def load_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def parse_input(_input: str) -> list[list[str]]:
    return [list(row.strip("\n")) for row in _input.strip("\n").split("\n")]


def search_word_horizontal(matrix: list[list[str]], index: tuple[int, int], word: str) -> bool:
    if len(word) <= len(matrix[index[0]][index[1] :]):
        return ("".join([matrix[index[0]][index[1] + i] for i in range(len(word))]) == word)
    else:
        return False


def search_word_vertical(matrix: list[list[str]], index: tuple[int, int], word: str) -> bool:
    if len(word) <= len(matrix[index[0] :]):
        return ("".join([matrix[index[0] + i][index[1]] for i in range(len(word))]) == word)
    else:
        return False


def search_word_diagonal(matrix: list[list[str]], index: tuple[int, int], word: str) -> bool:
    if len(word) <= len(matrix[index[0]][index[1] :]) and len(word) <= len(matrix[index[0] :]):
        return ("".join([matrix[index[0] + i][index[1] + i] for i in range(len(word))]) == word)
    else:
        return False


def search_word_reverse_diagonal(matrix: list[list[str]], index: tuple[int, int], word: str) -> bool:
    if len(word) <= len(matrix[index[0] :]) and index[1] - len(word) >= -1:
        return ("".join([matrix[index[0] + i][index[1] - i] for i in range(len(word))]) == word)
    else:
        return False


def count_word(matrix: list[list[str]], word: str) -> int:
    word_count = 0
    word_reversed = "".join(reversed(list(word)))
    for i, _ in enumerate(matrix):
        for j, _ in enumerate(matrix[i]):
            word_count += sum([
                search_word_horizontal(matrix=matrix, index=(i, j), word=word),
                search_word_horizontal(matrix=matrix, index=(i, j), word=word_reversed),
                search_word_vertical(matrix=matrix, index=(i, j), word=word),
                search_word_vertical(matrix=matrix, index=(i, j), word=word_reversed),
                search_word_diagonal(matrix=matrix, index=(i, j), word=word),
                search_word_diagonal(matrix=matrix, index=(i, j), word=word_reversed),
                search_word_reverse_diagonal(matrix=matrix, index=(i, j), word=word),
                search_word_reverse_diagonal(matrix=matrix, index=(i, j), word=word_reversed),
            ])
    return word_count


def search_x_mas(matrix: list[list[str]], index: tuple[int, int]) -> bool:
    if 0 < index[0] < len(matrix) - 1 and 0 < index[1] < len(matrix[index[0]]) - 1:
        if matrix[index[0]][index[1]] == "A":
            corners = [
                matrix[index[0] - 1][index[1] - 1],
                matrix[index[0] - 1][index[1] + 1],
                matrix[index[0] + 1][index[1] - 1],
                matrix[index[0] + 1][index[1] + 1],
            ]
            if (corners.count("M") == 2 and corners.count("S") == 2 and corners[0] != corners[-1]):
                return True
    return False


def count_x_mas(matrix: list[list[str]]) -> int:
    x_mas_count = 0
    for i, _ in enumerate(matrix):
        for j, _ in enumerate(matrix[i]):
            x_mas_count += sum([search_x_mas(matrix=matrix, index=(i, j))])
    return x_mas_count


def main() -> None:
    test_data: list[list[str]] = [
        ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
        ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
        ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M"],
        ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
        ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M"],
        ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A"],
        ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S"],
        ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A"],
        ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M"],
        ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"],
    ]
    assert count_word(matrix=test_data, word="XMAS") == 18
    assert count_x_mas(matrix=test_data) == 9
    matrix = parse_input(_input=load_input(filename="day_04_input.txt"))
    answer_part_one = count_word(matrix=matrix, word="XMAS")
    answer_part_two = count_x_mas(matrix=matrix)
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()
