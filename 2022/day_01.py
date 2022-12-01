def load_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def parse_input(_input: str) -> list[list[int]]:
    elves = [[int(calories) for calories in elf.split("\n")] for elf in _input.strip().split("\n\n")]
    return elves


def calculate_calories(elves: list[list[int]]) -> list[int]:
    return [sum(elf) for elf in elves]


def find_max_calories(calories: list[int], top: int=1) -> int:
    return sum(sorted(calories, reverse=True)[:top])


def main() -> None:
    test_data: str = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
    assert find_max_calories(calculate_calories(parse_input(test_data))) == 24000
    assert find_max_calories(calculate_calories(parse_input(test_data)), 3) == 45000
    calories = parse_input(load_input("day_01_input.txt"))
    answer_part_one = find_max_calories(calculate_calories(calories))
    answer_part_two = find_max_calories(calculate_calories(calories), 3)
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()
