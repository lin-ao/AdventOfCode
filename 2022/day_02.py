def load_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read().strip()
        

def parse_input(_input: str) -> list[tuple[str, str]]:
    return [tuple(row.split(" ")) for row in _input.split("\n")]
    

def get_outcome(game: tuple[str, str]) -> int:
    mappings = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    opponent, player = game
    try:
        match mappings[player] - mappings[opponent]:
            case 0:
                return mappings[player] + 3
            case 1 | -2:
                return mappings[player] + 6
            case -1 | 2:
                return mappings[player]
            case _:
                raise Exception
    except Exception:
        raise
            

def choose_outcome(game: tuple[str, str]) -> int:
    mappings = {"A": 1, "B": 2, "C": 3}
    score_winnning = {"A": 2, "B": 3, "C": 1}
    score_losing = {"A": 3, "B": 1, "C": 2}
    opponent, player = game
    try:
        match player:
            case "X":
                return score_losing[opponent]
            case "Y":
                return mappings[opponent] + 3
            case "Z":
                return score_winnning[opponent] + 6
            case _:
                raise Exception
    except Exception:
        raise


def main() -> None:
    test_data: str = "A Y\nB X\nC Z"
    assert sum([get_outcome(game) for game in parse_input(test_data)]) == 15
    assert sum([choose_outcome(game) for game in parse_input(test_data)]) == 12
    games = parse_input(load_input("day_02_input.txt"))
    answer_part_one = sum([get_outcome(game) for game in games])
    answer_part_two = sum([choose_outcome(game) for game in games])
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()
