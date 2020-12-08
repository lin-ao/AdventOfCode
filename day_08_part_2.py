from day_08_part_1 import load_input


class HandheldGameConsole:
    def __init__(self, logic: list[tuple]) -> None:
        self.logic = logic
        self.accumulator = 0
        self.step = 0
        self.execute()

    def acc(self, increment: int) -> None:
        self.accumulator += increment
        self.step += 1
        self.execute()

    def jmp(self, offset: int) -> None:
        self.step += offset
        self.execute()

    def nop(self, _) -> None:
        self.step += 1
        self.execute()

    def execute(self) -> None:
        try:
            getattr(self, self.logic[self.step][0])(self.logic[self.step][1])
        except IndexError:
            pass


def fix_code(code: list[tuple], checked=None) -> list[tuple]:
    if checked is None:
        checked = []
    switches = {"jmp", "nop"}
    index = code.index(next(filter(lambda x: (x[0] == "jmp" or x[0] == "nop") and code.index(x) not in checked, code)))
    code[index] = (*switches - {code[index][0]}, code[index][1])
    try:
        HandheldGameConsole(code)
    except RecursionError:
        code[index] = (*switches - {code[index][0]}, code[index][1])
        checked.append(index)
        fix_code(code, checked)
    return code


def main() -> None:
    code = fix_code(load_input("day_08_input.txt"))
    answer = HandheldGameConsole(code).accumulator
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
