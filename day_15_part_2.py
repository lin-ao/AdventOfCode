from day_15_part_1 import load_input, game


def main() -> None:
    answer = game(load_input("day_15_input.txt"), 30000000)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
