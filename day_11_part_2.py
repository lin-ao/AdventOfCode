from day_11_part_1 import load_input, is_occupied


def is_seat(seat: tuple[int, int], seating: list[list[str]]):
    return seating[seat[0]][seat[1]] == "#" or seating[seat[0]][seat[1]] == "L"


def generate_adjacent(seat: tuple[int, int], seating: list[list[str]]) -> list[tuple[int, int]]:
    nw = next((seat for seat in reversed([(seat[0] - i, seat[1] - i) for i in range(min(seat[0], seat[1]), 0, -1)])
               if is_seat(seat, seating)), None)
    n = next((seat for seat in reversed([(seat[0] - i, seat[1]) for i in range(seat[0], 0, -1)])
              if is_seat(seat, seating)), None)
    ne = next((seat for seat in reversed([(seat[0] - i, seat[1] + i) for i in range(min(seat[0], len(seating[seat[0]]) - 1 - seat[1]), 0, -1)])
               if is_seat(seat, seating)), None)
    e = next((seat for seat in reversed([(seat[0], seat[1] + i) for i in range(len(seating[seat[0]]) - 1 - seat[1], 0, -1)])
              if is_seat(seat, seating)), None)
    se = next((seat for seat in reversed([(seat[0] + i, seat[1] + i) for i in range(min(len(seating) - 1 - seat[0], len(seating[seat[0]]) - 1 - seat[1]), 0, -1)])
               if is_seat(seat, seating)), None)
    s = next((seat for seat in reversed([(seat[0] + i, seat[1]) for i in range(len(seating) - 1 - seat[0], 0, -1)])
              if is_seat(seat, seating)), None)
    sw = next((seat for seat in reversed([(seat[0] + i, seat[1] - i) for i in range(min(len(seating) - 1 - seat[0], seat[1]), 0, -1)])
               if is_seat(seat, seating)), None)
    w = next((seat for seat in reversed([(seat[0], seat[1] - i) for i in range(seat[1], 0, -1)])
              if is_seat(seat, seating)), None)
    return [x for x in [nw, n, ne, e, se, s, sw, w] if x is not None]


def count_adjacent(seat: tuple[int, int], seating: list[list[str]]) -> int:
    return sum(is_occupied(seat, seating) for seat in generate_adjacent(seat, seating))


def update_seat(seat: tuple[int, int], seating: list[list[str]], updated_seating: list[list[str]]) -> None:
    if seating[seat[0]][seat[1]] == "L" and count_adjacent(seat, seating) == 0:
        updated_seating[seat[0]][seat[1]] = "#"
    elif seating[seat[0]][seat[1]] == "#" and count_adjacent(seat, seating) >= 5:
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
    return sum(
        is_occupied((row, col), seating) for row in range(0, len(seating)) for col in range(0, len(seating[row])))


def main() -> None:
    seating = load_input("day_11_input.txt")
    updated_seating = update_seats(seating)[0]
    answer = count_occupied(updated_seating)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
