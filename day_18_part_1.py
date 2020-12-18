from collections import defaultdict
from typing import Iterable


def load_input(file_path: str) -> Iterable[str]:
    with open(file_path, "r") as file:
        for line in file:
            yield line


def calculate(calc: str) -> int:
    brackets_dict = defaultdict(lambda: 0)
    closing_brackets = 0
    calc = calc.split(" ")
    parsed_calc = []
    for part in reversed(calc):
        if part.isdigit():
            parsed_calc.append(part + ")")
            brackets_dict[closing_brackets] += 1
        elif part.endswith(")"):
            parsed_calc.append(part + ")")
            brackets_dict[closing_brackets] += 1
            closing_brackets += part.count(")")
        elif part.startswith("("):
            counter = 0
            for _ in range(part.count("(")):
                counter += brackets_dict[closing_brackets]
                brackets_dict.pop(closing_brackets)
                closing_brackets -= 1
            parsed_calc.append(part.rjust(len(part) + counter, "("))
        else:
            parsed_calc.append(part)
    parsed_calc[-1] = parsed_calc[-1].rjust(len(parsed_calc[-1]) + brackets_dict[closing_brackets], "(")
    return eval(" ".join(reversed(parsed_calc)))


def main() -> None:
    inputs = load_input("day_18_input.txt")
    answer = sum(calculate(calculation) for calculation in inputs)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
