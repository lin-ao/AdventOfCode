import re
from collections import defaultdict
from typing import Iterable


def load_input(file_path: str) -> Iterable[str]:
    with open(file_path, "r") as file:
        for line in file:
            yield line


def parse_mask(line: str) -> str:
    parser = re.compile(r"^mask = ([X01]{36})\n$")
    bitmask = parser.match(line).groups()[0]
    return bitmask


def parse_memory(line: str) -> tuple[int, int]:
    parser = re.compile(r"^mem\[(\d+)] = (\d+)\n$")
    memory, value = map(int, parser.match(line).groups())
    return memory, value


def apply_bitmask(bitmask: str, value: int) -> int:
    value = list(bin(value)[2:].zfill(36))
    for i, bit in enumerate(bitmask):
        if bit.isdigit():
            value[i] = bit
    return int("".join(value), 2)


def initialization(commands: Iterable[str]) -> dict[int, int]:
    memory_space = defaultdict(int)
    bitmask = ""
    for line in commands:
        if line.startswith("mask"):
            bitmask = parse_mask(line)
        else:
            memory, value = parse_memory(line)
            memory_space[memory] = apply_bitmask(bitmask, value)
    return memory_space


def main() -> None:
    memory_space = initialization(load_input("day_14_input.txt"))
    answer = sum(memory_space.values())
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
