from collections import defaultdict
from re import compile


def load_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()
        

def parse_input(_input: str) -> list[str]:
    return _input.rstrip().split("\n\n")


def parse_stacks(stacks: str) -> defaultdict[int, list[str]]:
    parsed_stacks = defaultdict(lambda: list())
    row_pattern = compile(r"[\[ ]{1}([A-Z ]{1})[\] ]? ?")
    for row in stacks.split("\n")[-2::-1]:
        for index, column in enumerate(row_pattern.findall(row)):
            if column != " ":
                parsed_stacks[index+1].append(column)
    return parsed_stacks


def parse_instructions(instructions: str) -> list[tuple[int, int, int]]:
    pattern = compile(r"^move (\d+) from (\d+) to (\d+)$")
    return [tuple(map(int, pattern.match(instruction).groups())) for instruction in instructions.split("\n")]


def process_stacks(stacks: defaultdict[int, list[str]], instructions: list[tuple[int, int, int]]) -> defaultdict[int, list[str]]:
    for number, source, target in instructions:
        for _ in range(number):
            stacks[target].append(stacks[source].pop())
    return stacks


def process_stacks_ordered(stacks: defaultdict[int, list[str]], instructions: list[tuple[int, int, int]]) -> defaultdict[int, list[str]]:
    for number, source, target in instructions:
        stacks[target] += (stacks[source][-number:])
        stacks[source] = stacks[source][:-number]
    return stacks


def get_stack_tops(stacks: defaultdict[int, list[str]]) -> str:
    return "".join([stacks[key].pop() for key in stacks])


def main() -> None:
    test_data: str = "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2"
    test_stacks_raw, test_instructions_raw = parse_input(test_data)
    assert get_stack_tops(process_stacks(parse_stacks(test_stacks_raw), parse_instructions(test_instructions_raw))) == "CMZ"
    assert get_stack_tops(process_stacks_ordered(parse_stacks(test_stacks_raw), parse_instructions(test_instructions_raw))) == "MCD"
    stacks_raw, instructions_raw = parse_input(load_input("day_05_input.txt"))
    answer_part_one = get_stack_tops(process_stacks(parse_stacks(stacks_raw), parse_instructions(instructions_raw)))
    answer_part_two = get_stack_tops(process_stacks_ordered(parse_stacks(stacks_raw), parse_instructions(instructions_raw)))
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()
