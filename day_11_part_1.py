def load_input(file_path: str) -> list[list[str]]:
    with open(file_path, "r") as file:
        return [list(line.rstrip("\n")) for line in file]


def is_occupied(seat: tuple[int, int], seating: list[[list[str]]]):
    return seating[seat[0]][seat[1]] == "#"


def generate_adjacent(seat: tuple[int, int], seating: list[list[str]]) -> list[tuple[int, int]]:
    adjacent = [(seat[0] - 1, seat[1] - 1), (seat[0] - 1, seat[1]), (seat[0] - 1, seat[1] + 1), (seat[0], seat[1] - 1),
                (seat[0], seat[1] + 1), (seat[0] + 1, seat[1] - 1), (seat[0] + 1, seat[1]), (seat[0] + 1, seat[1] + 1)]
    return filter(lambda x: True if 0 <= x[0] < len(seating) and 0 <= x[1] < len(seating[seat[0]]) else False, adjacent)


def count_adjacent(seat: tuple[int, int], seating: list[list[str]]) -> int:
    return sum(is_occupied(seat, seating) for seat in generate_adjacent(seat, seating))


def update_seat(seat: tuple[int, int], seating: list[list[str]], updated_seating: list[list[str]]) -> None:
    if seating[seat[0]][seat[1]] == "L" and count_adjacent(seat, seating) == 0:
        updated_seating[seat[0]][seat[1]] = "#"
    elif seating[seat[0]][seat[1]] == "#" and count_adjacent(seat, seating) >= 4:
        updated_seating[seat[0]][seat[1]] = "L"
    else:
        pass


def update_seats(seating: list[list[str]], unchanged=False) -> tuple[list[list[str]], bool]:
    unchanged = unchanged
    updated_seating = [[seat for seat in row] for row in seating]
    if unchanged:
        return updated_seating, unchanged
    else:
        for row in range(0, len(seating)):
            for col in range(0, len(seating[row])):
                update_seat((row, col), seating, updated_seating)
        unchanged = seating == updated_seating
        return update_seats(updated_seating, unchanged)


def count_occupied(seating: list[list[str]]) -> int:
    return sum(is_occupied((row, col), seating) for row in range(0, len(seating)) for col in range(0, len(seating[row])))


def main() -> None:
    seating = load_input("day_11_input.txt")
    updated_seating = update_seats(seating)[0]
    answer = count_occupied(updated_seating)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
