def convert_position(boarding_pass: str) -> tuple[int, int]:
    row = int(boarding_pass.replace("F", "0").replace("B", "1")[:7], 2)
    col = int(boarding_pass.replace("L", "0").replace("R", "1")[7:], 2)
    return row, col


def calculate_seat_id(position: tuple) -> int:
    return position[0] * 8 + position[1]


def main() -> None:
    with open("day_05_input.txt", "r") as file:
        answer = max(calculate_seat_id(convert_position(line)) for line in file)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
