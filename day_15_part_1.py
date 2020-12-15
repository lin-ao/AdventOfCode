def load_input(file_path: str) -> dict[int, int]:
    with open(file_path, "r")as file:
        file = file.read()
        number_dict = {int(item): i + 1 for i, item in enumerate(file.rstrip("\n").split(","))}
        return number_dict


def game(number_dict: dict[int, int], turns: int) -> int:
    i = len(number_dict)
    last_number = -1
    while i < turns:
        i += 1
        if last_number in number_dict:
            last_spoken = number_dict[last_number]
            number_dict[last_number] = i - 1
            last_number = number_dict[last_number] - last_spoken
        else:
            number_dict[last_number] = i - 1
            last_number = 0
    return last_number


def main() -> None:
    answer = game(load_input("day_15_input.txt"), 2020)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
