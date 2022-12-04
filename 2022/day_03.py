from itertools import zip_longest


def load_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read().strip()
        

def parse_input(_input: str) -> list[str]:
    return _input.split("\n")


def get_items(backpack: str) -> list[str]:
    return list(backpack)


def get_compartments(backpack: list[str]) -> list[str]:
    return list(map(lambda x: "".join(x), zip_longest(*[iter(backpack)]*(len(backpack)//2))))


def get_groups(backpacks: list[str]) -> list[list[str]]:
    return [list(group) for group in zip_longest(*[iter(backpacks)]*3)]


def find_common_item(compartments: list[str]) -> set[str]:
    return set.intersection(*map(set, compartments))


def get_score(items: set[str]) -> int:
    return sum([ord(item)%32 if item.islower() else ord(item)%32+26 for item in items])


def main() -> None:
    test_data: str = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw"
    assert sum([get_score(item) for item in [find_common_item(get_compartments(get_items(backpack))) for backpack in parse_input(test_data)]]) == 157
    assert sum([get_score(item) for item in [find_common_item(group) for group in get_groups(parse_input(test_data))]]) == 70
    backpacks = parse_input(load_input("day_03_input.txt"))
    answer_part_one = sum([get_score(item) for item in [find_common_item(get_compartments(get_items(backpack))) for backpack in backpacks]])
    answer_part_two = sum([get_score(item) for item in [find_common_item(group) for group in get_groups(backpacks)]])
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()
