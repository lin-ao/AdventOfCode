def load_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read().strip()
        

def parse_input(_input: str) -> list[list[tuple[int, int]]]:
    return [[tuple(map(int,(pair.split("-")))) for pair in row.split(",")] for row in _input.split("\n")]


def if_contains(pair: list[tuple[int, int]]) -> bool:
    x, y = pair
    return (x[0] >= y[0] and x[1] <= y[1]) or (x[0] <= y[0] and x[1] >= y[1])


def if_overlap(pair: list[tuple[int, int]]) -> bool:
    x, y = pair
    return max(x[0], y[0]) <= min(x[1], y[1])


def main() -> None:
    test_data: str = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"
    assert sum([if_contains(pair) for pair in parse_input(test_data)]) == 2
    assert sum([if_overlap(pair) for pair in parse_input(test_data)]) == 4
    pairs = parse_input(load_input("day_04_input.txt"))
    answer_part_one = sum([if_contains(pair) for pair in pairs])
    answer_part_two = sum([if_overlap(pair) for pair in pairs])
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()
