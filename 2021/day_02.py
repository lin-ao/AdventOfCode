import re


class SubmarineOne:
    def __init__(self, course: list[tuple[str, int]]) -> None:
        self.course: list[tuple[str, int]] = course
        self.horizontal: int = 0
        self.depth: int = 0
        self.position: int = 0
        self.execute()

    def forward(self, distance: int) -> None:
        self.horizontal += distance

    def down(self, distance: int) -> None:
        self.depth += distance

    def up(self, distance: int) -> None:
        self.depth -= distance

    def execute(self) -> None:
        for (command, value) in self.course:
            getattr(self, command)(int(value))
        self.position = self.horizontal * self.depth


class SubmarineTwo:
    def __init__(self, course: list[tuple[str, int]]) -> None:
        self.course: list[tuple[str, int]] = course
        self.horizontal: int = 0
        self.depth: int = 0
        self.aim: int = 0
        self.position: int = 0
        self.execute()

    def forward(self, distance: int) -> None:
        self.horizontal += distance
        self.depth += self.aim * distance

    def down(self, distance: int) -> None:
        self.aim += distance

    def up(self, distance: int) -> None:
        self.aim -= distance

    def execute(self) -> None:
        for (command, value) in self.course:
            getattr(self, command)(int(value))
        self.position = self.horizontal * self.depth


def load_input(file_path: str) -> list[tuple[str, int]]:
    with open(file_path, "r") as file:
        parser = re.compile(r"^([a-z]+) ([\d]{1})\n$")
        return [(parser.match(line).groups()) for line in file]


def main() -> None:
    test_data: list[tuple[str, int]] = [("forward", 5), ("down", 5), ("forward", 8), ("up", 3), ("down", 8), ("forward", 2)]
    assert SubmarineOne(test_data).position == 150
    assert SubmarineTwo(test_data).position == 900

    course: list[tuple[str, int]] = load_input("day_02_input.txt")
    answer_part_one: int = SubmarineOne(course).position
    answer_part_two: int = SubmarineTwo(course).position
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()
