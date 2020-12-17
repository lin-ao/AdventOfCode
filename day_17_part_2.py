from collections import defaultdict
from itertools import product
from typing import Any


def load_input(file_path: str) -> list[tuple[int, int, int, int]]:
    with open(file_path, "r") as file:
        pocket = [(x, y, 0, 0) for x, row in enumerate(file) for y, col in enumerate(row) if col == "#"]
        return pocket


def neighbors(point: tuple[int, int, int, int]) -> list[tuple[Any]]:
    w = [point[0] - 1, point[0], point[0] + 1]
    x = [point[1] - 1, point[1], point[1] + 1]
    y = [point[2] - 1, point[2], point[2] + 1]
    z = [point[3] - 1, point[3], point[3] + 1]
    _neighbors = list(product(w, x, y, z))
    _neighbors.remove(point)
    return _neighbors


def update(pocket_dimension: list[tuple[int, int, int, int]], cycle: int) -> int:
    if cycle > 0:
        possible = defaultdict(lambda: 0)
        updated_pocket_dimension = []
        for point in pocket_dimension:
            for neighbor in neighbors(point):
                possible[neighbor] += 1
        for point in possible:
            if point in pocket_dimension and (possible[point] == 2 or possible[point] == 3):
                updated_pocket_dimension.append(point)
            elif point not in pocket_dimension and possible[point] == 3:
                updated_pocket_dimension.append(point)
            else:
                pass
        return update(updated_pocket_dimension, cycle - 1)
    else:
        return len(pocket_dimension)


def main() -> None:
    pocket_dimension = load_input("day_17_input.txt")
    answer = update(pocket_dimension, 6)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
