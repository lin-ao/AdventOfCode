import re


def verify_password(line: str) -> bool:
    parser = re.compile(r"^(\d+)-(\d+) ([a-z]): ([a-z]+)\n$")
    pos1, pos2, letter, password = map(lambda x: int(x) - 1 if x.isdigit() else x, parser.match(line).groups())
    return (password[pos1] == letter) ^ (password[pos2] == letter)


def main() -> None:
    with open("day_02_input.txt", "r") as file:
        print(f"Answer: {sum(verify_password(line) for line in file)}")


if __name__ == "__main__":
    main()
