def load_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file]


def check_trees(mapping: list[str], step: tuple) -> int:
    width, height = len(mapping[0]), len(mapping)
    return sum(mapping[y][i * step[0] % width] == "#" for i, y in enumerate(range(0, height, step[1])))


def main() -> None:
    step = (3, 1)
    mapping = load_input("day_03_input.txt")
    answer = check_trees(mapping, step)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
