from typing import Iterable


class Transform:
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return Transform(self.value * other.value)

    def __mul__(self, other):
        return Transform(self.value + other.value)


def load_input(file_path: str) -> Iterable[str]:
    with open(file_path, "r") as file:
        for line in file:
            yield line


def calculate(calculation: str) -> int:
    for d in range(10):
        calculation = calculation.replace(f"{d}", f"Transform({d})")
    calculation = calculation.replace("*", "-").replace("+", "*")
    return eval(calculation, {"Transform": Transform}).value


def main() -> None:
    inputs = load_input("day_18_input.txt")
    answer = sum(calculate(calculation) for calculation in inputs)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
