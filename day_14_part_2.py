from collections import defaultdict
from itertools import combinations
from typing import Iterable

from day_14_part_1 import load_input, parse_mask, parse_memory


def find_char(string: Iterable[str], character: str) -> list[int]:
    return [i for i, char in enumerate(string) if char == character]


def apply_bitmask(bitmask: str, memory: int) -> set[int]:
    memory = list(bin(memory)[2:].zfill(36))
    for i, bit in enumerate(bitmask):
        if bit != "0":
            memory[i] = bit
    base = int("".join(memory).replace("X", "0"), 2)
    additives = list(map(lambda x: 2 ** x, find_char(reversed(memory), "X")))
    combs = [comb for i in range(len(additives) + 1) for comb in combinations(additives, i)]
    return {base + sum(comb) for comb in combs}


def initialization(commands: Iterable[str]) -> dict[int, int]:
    memory_space = defaultdict(int)
    bitmask = ""
    for line in commands:
        if line.startswith("mask"):
            bitmask = parse_mask(line)
        else:
            memory, value = parse_memory(line)
            for memory in apply_bitmask(bitmask, memory):
                memory_space[memory] = value
    return memory_space


def main() -> None:
    memory_space = initialization(load_input("day_14_input.txt"))
    answer = sum(memory_space.values())
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
