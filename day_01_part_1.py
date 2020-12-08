def load_input(file_path: str) -> list[int]:
    with open(file_path, "r") as file:
        return [int(line) for line in file]


def update_list(input_list: list[int], threshold: int) -> list[int]:
    return [number for number in input_list if number < threshold]


def part_1(input_list: list[int], expected_sum: int) -> int:
    input_half_1 = sorted([number for number in input_list if number <= expected_sum // 2])
    input_half_2 = sorted(set(input_list).symmetric_difference(input_half_1))
    for number in input_half_1:
        if expected_sum - number in input_half_2:
            return number * (expected_sum - number)
        else:
            input_half_2 = update_list(input_half_2, expected_sum - number)
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
