from math import prod

from day_01_part_1 import load_input


def find_valid_removals(adapters: list[int]) -> list[int]:
    unrestricted_removal = []
    restricted_removal = []
    for i in range(1, len(adapters) - 1):
        if adapters[i + 1] - adapters[i - 1] <= 3:
            if adapters[i - 1] in unrestricted_removal and adapters[i - 2] in unrestricted_removal \
                    and adapters[i + 1] - adapters[i - 3] > 3:
                unrestricted_removal.remove(adapters[i - 2])
                unrestricted_removal.remove(adapters[i - 1])
                restricted_removal.append((adapters[i - 2], adapters[i - 1], adapters[i]))
            elif adapters[i - 1] in unrestricted_removal and adapters[i + 1] - adapters[i - 2] > 3:
                unrestricted_removal.remove(adapters[i - 1])
                restricted_removal.append((adapters[i - 1], adapters[i]))
            else:
                unrestricted_removal.append(adapters[i])
    possible_unrestricted_removals = 2 ** len(unrestricted_removal)
    possible_restricted_removals = prod([2 ** len(item) - 1 for item in restricted_removal])
    return possible_unrestricted_removals * possible_restricted_removals


def main() -> None:
    adapters = sorted(load_input("day_10_input.txt"))
    adapters.insert(0, 0)
    answer = find_valid_removals(adapters)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
