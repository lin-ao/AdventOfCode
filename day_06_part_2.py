from functools import reduce
from typing import Iterable


def load_input(file_path: str) -> Iterable[list]:
    with open(file_path, "r") as file:
        for answer in file.read().rstrip("\n").split("\n\n"):
            yield answer.split("\n")


def count_answers(answers: list) -> int:
    return len(reduce(lambda x, y: x.intersection(y), map(set, answers)))


def main():
    answer = sum(count_answers(answer) for answer in load_input("day_06_input.txt"))
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
