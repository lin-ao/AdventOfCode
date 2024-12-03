import re


def load_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def parse_memory(corrupted_memory: str) -> list[tuple[str, str]]:
    memory = re.findall(r"mul\((\d+),(\d+)\)", corrupted_memory)
    return memory


def parse_enabled_memory(corrupted_memory: str) -> list[tuple[str, str]]:
    corrupted_memory = corrupted_memory.replace("\n", "")
    corrupted_memory = re.sub(r"don't\(\).*?do\(\)", "", corrupted_memory)
    corrupted_memory = re.sub(r"don't\(\).*$", "", corrupted_memory)
    memory = re.findall(r"mul\((\d+),(\d+)\)", corrupted_memory)
    return memory


def execute_memory(memory: list[tuple[str, str]]) -> int:
    return sum([int(a) * int(b) for a, b in memory])


def main() -> None:
    test_data_one: str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    test_data_two: str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert execute_memory(parse_memory(test_data_one)) == 161
    assert execute_memory(parse_enabled_memory(test_data_two)) == 48
    corrupted_memory = load_input(filename="day_03_input.txt")
    answer_part_one = execute_memory(memory=parse_memory(corrupted_memory=corrupted_memory))
    answer_part_two = execute_memory(memory=parse_enabled_memory(corrupted_memory=corrupted_memory))
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()
