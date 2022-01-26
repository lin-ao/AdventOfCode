from day_12_part_1 import load_input


class Ship:
    def __init__(self, course: list[tuple[str, int]]) -> None:
        self.course = course
        self.waypoint = [10, 1]
        self.position = [0, 0]
        self.distance = 0
        self.execute()

    def n(self, distance: int) -> None:
        self.waypoint[1] += distance

    def e(self, distance: int) -> None:
        self.waypoint[0] += distance

    def s(self, distance: int) -> None:
        self.waypoint[1] -= distance

    def w(self, distance: int) -> None:
        self.waypoint[0] -= distance

    def l(self, angle: int) -> None:
        for _ in range(0, angle // 90):
            self.waypoint[0], self.waypoint[1] = -self.waypoint[1], self.waypoint[0]

    def r(self, angle: int) -> None:
        for _ in range(0, angle // 90):
            self.waypoint[0], self.waypoint[1] = self.waypoint[1], -self.waypoint[0]

    def f(self, value: int) -> None:
        self.position[0] += value * self.waypoint[0]
        self.position[1] += value * self.waypoint[1]

    def execute(self) -> None:
        for (command, value) in self.course:
            getattr(self, command.lower())(int(value))
        self.distance = abs(self.position[0]) + abs(self.position[1])


def main() -> None:
    input_list = load_input("day_12_input.txt")
    answer = Ship(input_list).distance
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
