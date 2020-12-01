def load_input(file_path: str) -> set:
    with open(file_path, "r") as inp:
        return [int(line.strip()) for line in inp]


def update_list(input_list: list, threshold: int) -> list:
    return [number for number in input_list if number > threshold]


def part_1(input_list: list, expected_sum: int) -> int:
    input_half_1 = sorted([number for number in input_list if number <= expected_sum // 2])
    input_half_2 = sorted(set(input_list).symmetric_difference(input_half_1))
    for number in input_half_1:
        if expected_sum - number in input_half_2:
            return number * (expected_sum - number)
        else:
            input_half_2 = update_list(input_half_2, number)
    return 0


def main() -> None:
    input_list = load_input("day_01_input.txt")
    answer = part_1(input_list, 2020)
    if not answer == 0:
        print(f"Answer: {answer}")
    else:
        print("No answer was found.")


if __name__ == "__main__":
    main()
