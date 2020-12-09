from day_01_part_1 import load_input


def check_for_sum(numbers: list[int], target: int) -> bool:
    return any(target - number in numbers for number in numbers)


def find_number(numbers: list[int], preamble: int) -> int:
    for index, number in enumerate(numbers[preamble:], preamble):
        if not check_for_sum(numbers[index-preamble:index], number):
            return number


def main() -> None:
    numbers = load_input("day_09_input.txt")
    answer = find_number(numbers, preamble=25)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
