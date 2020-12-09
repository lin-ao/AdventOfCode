from day_01_part_1 import load_input
from day_09_part_1 import find_number


def find_number_range(numbers: list[int], target: int) -> int:
    number_range = []
    for number in numbers:
        if sum(number_range) < target:
            number_range.append(number)
        elif sum(number_range) > target:
            while sum(number_range) > target:
                number_range.pop(0)
            if sum(number_range) == target:
                return min(number_range) + max(number_range)
            else:
                number_range.append(number)
        else:
            return min(number_range) + max(number_range)


def main():
    numbers = load_input("day_09_input.txt")
    target = find_number(numbers, preamble=25)
    answer = find_number_range(numbers, target)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
