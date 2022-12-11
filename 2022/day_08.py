from typing import Union


def load_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()
        

def parse_input(_input: str) -> list[list[int]]:
    return [[int(char) for char in row] for row in _input.rstrip().split("\n")]


def is_visible(tree: int, indexes: tuple[int, int], row: list[int], column: tuple[int]) -> bool:
    visible_from_top = tree > max(column[:indexes[0]], default=-1)
    visible_from_bottom = tree > max(column[indexes[0]+1:], default=-1)
    visible_from_left = tree > max(row[:indexes[1]], default=-1)
    visible_from_right = tree > max(row[indexes[1]+1:], default=-1)
    return visible_from_top or visible_from_bottom or visible_from_left or visible_from_right


def count_is_visibles(rows: list[list[int]]) -> int:
    columns = list(zip(*rows))
    return sum([is_visible(column, (row_index, column_index), row, columns[column_index]) for row_index, row in enumerate(rows) for column_index, column in enumerate(row)])


def count_visible_trees(current: int, trees: Union[list[int], tuple[int]]) -> int:
    count = 0
    for tree in trees:
        if current > tree:
            count += 1
        else:
            return count + 1
    else:
        return count
        
    
def calculate_visibility(tree: int, indexes: tuple[int, int], row: list[int], column: tuple[int]) -> int:
    visibility_to_top = count_visible_trees(tree, list(reversed(column[:indexes[0]])))
    visibility_to_bottom = count_visible_trees(tree, column[indexes[0]+1:])
    visibility_to_left = count_visible_trees(tree, list(reversed(row[:indexes[1]])))
    visibility_to_right = count_visible_trees(tree, row[indexes[1]+1:])
    return visibility_to_top * visibility_to_bottom * visibility_to_left * visibility_to_right


def calculate_visibilities(rows: list[list[int]]) -> list[int]:
    columns = list(zip(*rows))
    return [calculate_visibility(column, (row_index, column_index), row, columns[column_index]) for row_index, row in enumerate(rows) for column_index, column in enumerate(row)]


def main() -> None:
    test_data: str = "30373\n25512\n65332\n33549\n35390"
    assert count_is_visibles(parse_input(test_data)) == 21
    assert max(calculate_visibilities(parse_input(test_data))) == 8
    trees = parse_input(load_input("day_08_input.txt"))
    answer_part_one = count_is_visibles(trees)
    answer_part_two = max(calculate_visibilities(trees))
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()
