from typing import Iterable


def load_input(file_path: str) -> Iterable[str]:
    with open(file_path, "r") as file:
        for answer in file.read().split("\n\n"):
            yield answer.replace("\n", "")


def count_answers(answers: str) -> int:
    return len(set(answers))


def main() -> None:
    answer = sum(count_answers(answer) for answer in load_input("day_06_input.txt"))
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
