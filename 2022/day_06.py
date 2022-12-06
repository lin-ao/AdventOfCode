def load_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read().strip()


def get_marker(stream: str, number: int=4) -> int:
    stack = []
    for index, char in enumerate(stream):
        if len(stack) == number:
            return index
        elif char in stack:
            stack = stack[stack.index(char)+1:]
            stack.append(char)
        else:
            stack.append(char)
    else:
        return -1


def main() -> None:
    assert get_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert get_marker("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert get_marker("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert get_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert get_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11
    assert get_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert get_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert get_marker("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert get_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert get_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26
    answer_part_one = get_marker(load_input("day_06_input.txt"))
    answer_part_two= get_marker(load_input("day_06_input.txt"), 14)
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()
