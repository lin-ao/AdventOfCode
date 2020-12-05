from day_03_part_1 import load_input
from day_05_part_1 import convert_position, calculate_seat_id


def find_empty_seat(boarding_passes: list) -> int:
    seat_ids = sorted([calculate_seat_id(convert_position(boarding_pass)) for boarding_pass in boarding_passes])
    seat = int(*{seat for seat in range(seat_ids[0], seat_ids[-1] + 1)}.symmetric_difference(seat_ids))
    return seat


def main() -> None:
    boarding_passes = load_input("day_05_input.txt")
    empty_seat = find_empty_seat(boarding_passes)
    print(f"Answer: {empty_seat}")


if __name__ == "__main__":
    main()
