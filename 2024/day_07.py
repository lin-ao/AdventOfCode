from functools import lru_cache
from itertools import product , zip_longest


def load_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def parse_input(_input: str) -> list[list[str]]:
    return [(int(operation.strip().split(': ')[0]), list(map(int, operation.strip().split(': ')[1].split(' ')))) for operation in _input.strip().split('\n')]


@lru_cache
def generate_operators(symbols: tuple[str], number: int) -> list[tuple[str, ...]]:
    return list(product(symbols, repeat=number))


def generate_operation(operands: list[str], operators: list[str]) -> list[str]:
    return [item for pair in zip_longest(operands, operators, fillvalue=None) for item in pair if item]


def evaluate_in_order(operation: str) -> int:
    result = operation[0]
    for index, operand in enumerate(operation[1::2]):
        if operand == '+':
            result += operation[index * 2 + 2]
        elif operand == '*':
            result *= operation[index * 2 + 2]
        elif operand == '||':
            result = int(str(result) + str(operation[index * 2 + 2]))
    return result


def sum_correct_operations(operations: list[tuple[int, list[int]]], operators: tuple[str]) -> int:
    output = 0
    for operation in operations:
        result, operands = operation
        operators_sets = generate_operators(symbols=operators, number=len(operands) - 1)
        for operators_set in operators_sets:
            formatted_operation = generate_operation(operands=operands, operators=operators_set)
            if evaluate_in_order(operation=formatted_operation) == result:
                output += result
                break
    return output


def main() -> None:
    test_data: list[tuple[int, list[int]]] = [
        (190, [10, 19]),
        (3267, [81, 40, 27]),
        (83, [17, 5]),
        (156, [15, 6]),
        (7290, [6, 8, 6, 15]),
        (161011, [16, 10, 13]),
        (192, [17, 8, 14]),
        (21037, [9, 7, 18, 13]),
        (292, [11, 6, 16, 20]),
    ]
    assert sum_correct_operations(operations=test_data, operators=('+', '*')) == 3749
    assert sum_correct_operations(operations=test_data, operators=('+', '*', '||')) == 11387
    operations = parse_input(_input=load_input(filename="day_07_input.txt"))
    answer_part_one = sum_correct_operations(operations=operations, operators=('+', '*'))
    answer_part_two = sum_correct_operations(operations=operations, operators=('+', '*', '||'))
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()
