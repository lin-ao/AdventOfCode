import re


class Ship:
    def __init__(self, course: list[tuple[str, int]]) -> None:
        self.course = course
        self.facing = 90
        self.position = [0, 0]
        self.distance = 0
        self.execute()

    def n(self, distance: int) -> None:
        self.position[1] += distance

    def e(self, distance: int) -> None:
        self.position[0] += distance

    def s(self, distance: int) -> None:
        self.position[1] -= distance

    def w(self, distance: int) -> None:
        self.position[0] -= distance

    def l(self, angle: int) -> None:
        self.facing -= angle
        self.facing %= 360

    def r(self, angle: int) -> None:
        self.facing += angle
        self.facing %= 360

    def f(self, distance: int) -> None:
        directions = ["n", "e", "s", "w"]
        getattr(self, directions[self.facing // 90])(distance)

    def execute(self) -> None:
        for (command, value) in self.course:
            getattr(self, command.lower())(int(value))
        self.distance = abs(self.position[0]) + abs(self.position[1])


def load_input(file_path: str) -> list[tuple[str, int]]:
    with open(file_path, "r") as file:
        parser = re.compile(r"^([A-Z]{1})(\d+)\n$")
        return [(parser.match(line).groups()) for line in file]


def main() -> None:
    input_list = load_input("day_12_input.txt")
    answer = Ship(input_list).distance
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
