from math import prod


def load_input(file_path: str) -> list[str]:
    with iter(open(file_path, "r")) as file:
        next(file)
        return [bus for bus in next(file).rstrip("\n").split(",")]


def find_with_remainder(mod: int, multiple: int, remainder: int) -> int:
    i = 1
    multiple = multiple % mod
    while multiple * i % mod != remainder:
        i += 1
    return i


def chinese_remainder_theorem(buses: list[str]) -> int:
    buses, b = zip(*[(int(bus), int(bus) - buses.index(bus)) for bus in buses if bus.isdigit()])
    n = [prod(buses) // bus for bus in buses]
    x = [find_with_remainder(buses[i], n[i], 1) for i in range(len(buses))]
    return sum(map(prod, zip(b, n, x))) % prod(buses)


def main() -> None:
    buses = load_input("day_13_input.txt")
    answer = chinese_remainder_theorem(buses)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
