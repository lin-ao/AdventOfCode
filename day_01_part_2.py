from day_01_part_1 import load_input, part_1


def part_2(input_list: list[int], expected_sum: int) -> int:
    for number in sorted(input_list):
        temporary_list = input_list[:]
        temporary_list.remove(number)
        answer = part_1(temporary_list, expected_sum - number)
        if not answer == 0:
            return answer * number
    return 0


def main() -> None:
    input_list = load_input("day_01_input.txt")
    answer = part_2(input_list, 2020)
    if not answer == 0:
        print(f"Answer: {answer}")
    else:
        print("No answer was found.")


if __name__ == "__main__":
    main()
