from collections import defaultdict
from itertools import permutations


def load_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def parse_input(_input: str) -> list[list[str]]:
    return [list(row.strip("\n")) for row in _input.strip("\n").split("\n")]


def generate_character_map(antenna_map: list[list[str]]) -> defaultdict[str, list[tuple[int, int]]]:
    character_map = defaultdict(list)
    for i, row in enumerate(antenna_map):
        for j, location in enumerate(row):
            if not location == '.':
                character_map[location].append((i, j))
    return character_map


def check_if_location_on_map(antenna_map: list[list[str]], location: tuple[int, int]) -> bool:
    return 0 <= location[0] < len(antenna_map) and 0 <= location[1] < len(antenna_map[location[0]])


def generate_antinode_locations(antenna_map: list[list[str]], antenna_one: tuple[int, int], antenna_two: tuple[int, int]) -> list[tuple[int, int]]:
    vector = (antenna_one[0] - antenna_two[0], antenna_one[1] - antenna_two[1])
    location_one = antenna_one[0] + vector[0], antenna_one[1] + vector[1]
    location_two = antenna_two[0] - vector[0], antenna_two[1] - vector[1]
    return [location for location in [location_one, location_two] if check_if_location_on_map(antenna_map=antenna_map, location=location)]


def generate_antinode_locations_with_resonant_harmonics(antenna_map: list[list[str]], antenna_one: tuple[int, int], antenna_two: tuple[int, int]) -> list[tuple[int, int]]:
    vector = (antenna_one[0] - antenna_two[0], antenna_one[1] - antenna_two[1])
    locations = [(antenna_one[0] + vector[0] * i, antenna_one[1] + vector[1]* i) for i in range(-len(antenna_map), len(antenna_map))]
    return [location for location in locations if check_if_location_on_map(antenna_map=antenna_map, location=location)]


def find_all_antinode_locations(antenna_map: list[list[str]], character_map: defaultdict[str, list[tuple[int, int]]], resonant_harmonics: bool=False) -> int:
    antinode_locations = []
    for character in character_map:
        antenna_pairs = list(permutations(character_map[character], 2))
        for antenna_pair in antenna_pairs:
            if resonant_harmonics:
                antinode_locations += generate_antinode_locations_with_resonant_harmonics(antenna_map=antenna_map, antenna_one=antenna_pair[0], antenna_two=antenna_pair[1])
            else:
                antinode_locations += generate_antinode_locations(antenna_map=antenna_map, antenna_one=antenna_pair[0], antenna_two=antenna_pair[1])
    return len(set(antinode_locations))


def main() -> None:
    test_data: list[list[str]] = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', 'A', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'A', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    ]
    assert find_all_antinode_locations(antenna_map=test_data, character_map=generate_character_map(antenna_map=test_data)) == 14
    assert find_all_antinode_locations(antenna_map=test_data, character_map=generate_character_map(antenna_map=test_data), resonant_harmonics=True) == 34
    antenna_map = parse_input(_input=load_input(filename="day_08_input.txt"))
    answer_part_one = find_all_antinode_locations(antenna_map=antenna_map, character_map=generate_character_map(antenna_map=antenna_map))
    answer_part_two = find_all_antinode_locations(antenna_map=antenna_map, character_map=generate_character_map(antenna_map=antenna_map), resonant_harmonics=True)
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()
