import re


def verify_password(line: str) -> bool:
    parser = re.compile(r"^(\d+)\-(\d+)\s(\w):\s(\w+)\s$")
    lower, upper, letter, password = map(lambda x: int(x) if x.isdigit() else x, parser.match(line).groups())
    return password.count(letter) in range(lower, upper + 1)


def main() -> None:
    with open("day_02_input.txt", "r") as file:
        print(f"Answer: {sum(verify_password(line) for line in file)}")


if __name__ == "__main__":
    main()
