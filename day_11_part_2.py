from typing import Iterable, Union

from day_11_part_1 import load_input, occupied


def is_seat(seat: tuple[int, int], seating: list[list[str]]):
    return seating[seat[0]][seat[1]] == "#" or seating[seat[0]][seat[1]] == "L"


def first_seat(seats: Iterable[tuple[int, int]], seating: list[list[str]]) -> Union[tuple[int, int], None]:
    return next((seat for seat in seats if is_seat(seat, seating)), None)


def generate_adjacent(seat: tuple[int, int], seating: list[list[str]]) -> list[tuple[int, int]]:
    nw = first_seat(((seat[0] - i, seat[1] - i) for i in range(1, min(seat[0], seat[1]) + 1)), seating)
    n = first_seat(((seat[0] - i, seat[1]) for i in range(1, seat[0] + 1)), seating)
    ne = first_seat(
        ((seat[0] - i, seat[1] + i) for i in range(1, min(seat[0] + 1, len(seating[seat[0]]) - seat[1]))), seating)
    e = first_seat(((seat[0], seat[1] + i) for i in range(1, len(seating[seat[0]]) - seat[1])), seating)
    se = first_seat(
        ((seat[0] + i, seat[1] + i) for i in range(1, min(len(seating) - seat[0], len(seating[seat[0]]) - seat[1]))),
        seating)
    s = first_seat(((seat[0] + i, seat[1]) for i in range(1, len(seating) - seat[0])), seating)
    sw = first_seat(((seat[0] + i, seat[1] - i) for i in range(1, min(len(seating) - seat[0], seat[1] + 1))), seating)
    w = first_seat(((seat[0], seat[1] - i) for i in range(1, seat[1] + 1)), seating)
    return [x for x in [nw, n, ne, e, se, s, sw, w] if x is not None]


def count_adjacent(seat: tuple[int, int], seating: list[list[str]]) -> int:
    return sum(occupied(seat, seating) for seat in generate_adjacent(seat, seating))


def update_seat(seat: tuple[int, int], seating: list[list[str]], updated_seating: list[list[str]]) -> None:
    if seating[seat[0]][seat[1]] == "L" and count_adjacent(seat, seating) == 0:
        updated_seating[seat[0]][seat[1]] = "#"
    elif seating[seat[0]][seat[1]] == "#" and count_adjacent(seat, seating) >= 5:
        updated_seating[seat[0]][seat[1]] = "L"
    else:
        pass


def update_seats(seating: list[list[str]]) -> list[list[str]]:
    updated_seating = [[seat for seat in row] for row in seating]
    for row in range(0, len(seating)):
        for col in range(0, len(seating[row])):
            update_seat((row, col), seating, updated_seating)
    if seating == updated_seating:
        return updated_seating
    else:
        return update_seats(updated_seating)


def count_occupied(seating: list[list[str]]) -> int:
    return sum(occupied((row, col), seating) for row in range(0, len(seating)) for col in range(0, len(seating[row])))


def main() -> None:
    seating = load_input("day_11_input.txt")
    updated_seating = update_seats(seating)
    answer = count_occupied(updated_seating)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
