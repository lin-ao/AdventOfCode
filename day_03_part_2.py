from math import prod
from day_03_part_1 import load_input, check_trees


def main() -> None:
    steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    mapping = load_input("day_03_input.txt")
    answer = prod(check_trees(mapping, step) for step in steps)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
