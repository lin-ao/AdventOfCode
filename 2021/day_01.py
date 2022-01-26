def load_input(filename: str) -> list[int]:
    with open(filename) as f:
        return [int(line.rstrip("\n")) for line in f]


def calculate_changes(measurements: list[int]) -> int:
    return sum(1 for index, measurement in enumerate(measurements) if measurement > measurements[index - 1])


def calculate_changes_sliding(measurements: list[int], window: int) -> int:
    measurements: list[int] = [sum(measurements[index:index + window]) for index, _ in enumerate(measurements[:-2])]
    return calculate_changes(measurements)


def main() -> None:
    test_data: list[int] = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert calculate_changes(test_data) == 7
    assert calculate_changes_sliding(test_data, 3) == 5

    measurements: list[int] = load_input("day_01_input.txt")
    answer_part_one: int = calculate_changes(measurements)
    answer_part_two: int = calculate_changes_sliding(measurements, 3)
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()
