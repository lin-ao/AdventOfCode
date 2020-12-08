class HandheldGameConsole:
    def __init__(self, logic: list[tuple]) -> None:
        self.logic = logic
        self.accumulator = 0
        self.step = 0
        self.performed = set()
        self.execute()

    def acc(self, increment: int) -> None:
        self.accumulator += increment
        self.performed.add(self.step)
        self.step += 1
        self.execute()

    def jmp(self, offset: int) -> None:
        self.performed.add(self.step)
        self.step += offset
        self.execute()

    def nop(self, _) -> None:
        self.performed.add(self.step)
        self.step += 1
        self.execute()

    def execute(self) -> None:
        if self.step in self.performed:
            pass
        else:
            getattr(self, self.logic[self.step][0])(self.logic[self.step][1])


def load_input(file_path: str) -> list[tuple]:
    with open(file_path, "r") as file:
        code_list = []
        for code in file:
            command, value = code.rstrip("\n").split(" ")
            code_list.append((command, int(value)))
        return code_list


def main() -> None:
    code = load_input("day_08_input.txt")
    answer = HandheldGameConsole(code).accumulator
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
