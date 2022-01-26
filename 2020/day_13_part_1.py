from operator import itemgetter


def load_input(file_path: str) -> tuple[int, list[int]]:
    with iter(open(file_path, "r")) as file:
        time = int(next(file).rstrip("\n"))
        buses = [int(bus) for bus in next(file).split(",") if bus.isdigit()]
        return time, buses


def least_waiting_time(time: int, buses: list[int]) -> int:
    least = max(((bus, time % bus) for bus in buses), key=itemgetter(1))
    return least[0] * (least[0] - least[1])


def main() -> None:
    time, buses = load_input("day_13_input.txt")
    answer = least_waiting_time(time, buses)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
