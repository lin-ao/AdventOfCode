import re

from day_04_part_1 import parse_credentials


def verify_birth_year(year: str) -> bool:
    try:
        return len(year) == 4 and 1920 <= int(year) <= 2002
    except ValueError:
        return False


def verify_issue_year(year: str) -> bool:
    try:
        return len(year) == 4 and 2010 <= int(year) <= 2020
    except ValueError:
        return False


def verify_expiration_year(year: str) -> bool:
    try:
        return len(year) == 4 and 2020 <= int(year) <= 2030
    except ValueError:
        return False


def verify_height(height: str) -> bool:
    try:
        if height.endswith("cm"):
            return 150 <= int(height.replace("cm", "")) <= 193
        elif height.endswith("in"):
            return 59 <= int(height.replace("in", "")) <= 76
        else:
            return False
    except ValueError:
        return False


def verify_hair_color(color: str) -> bool:
    parser = re.compile(r"^#[0-9a-f]{6}$")
    return parser.match(color)


def verify_eye_color(color: str) -> bool:
    colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    return color in colors


def verify_passport_id(pid: str) -> bool:
    try:
        int(pid)
        return len(pid) == 9
    except ValueError:
        return False


def verify_document(document: dict) -> bool:
    valid_document = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    if valid_document.symmetric_difference(document.keys()) in [{"cid"}, set()]:
        return all([verify_birth_year(document["byr"]), verify_issue_year(document["iyr"]),
                   verify_expiration_year(document["eyr"]), verify_height(document["hgt"]),
                   verify_hair_color(document["hcl"]), verify_eye_color(document["ecl"]),
                   verify_passport_id(document["pid"])])
    else:
        return False


def count_valid_documents(file_path: str) -> int:
    with open(file_path, "r") as file:
        return sum(verify_document(parse_credentials(document)) for document in file.read().split("\n\n"))


def main() -> None:
    answer = count_valid_documents("day_04_input.txt")
    print(answer)


if __name__ == "__main__":
    main()
