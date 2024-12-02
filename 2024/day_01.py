def load_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def parse_input(_input: str) -> list[list[int]]:
    list_one = []
    list_two = []
    for pair in _input.strip().split("\n"):
        id_one, id_two = pair.split("   ")
        list_one.append(int(id_one))
        list_two.append(int(id_two))
    return [list_one, list_two]


def calculate_distance(location_ids: list[list[int]]) -> int:
    return sum(abs(id_one - id_two) for id_one, id_two in zip(sorted(location_ids[0]), sorted(location_ids[1])))


def calculate_similarity(location_ids: list[list[int]]) -> int:
    similarity_score = 0
    for location_id in location_ids[0]:
        similarity_score += location_id * location_ids[1].count(location_id)
    return similarity_score


def main() -> None:
    test_data: str = [[3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]]
    assert calculate_distance(location_ids=test_data) == 11
    assert calculate_similarity(location_ids=test_data) == 31
    location_ids = parse_input(_input=load_input(filename="day_01_input.txt"))
    answer_part_one = calculate_distance(location_ids=location_ids)
    answer_part_two = calculate_similarity(location_ids=location_ids)
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()
