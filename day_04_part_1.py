import re


def parse_credentials(text: str) -> dict:
    parser = re.compile(r"([a-z]{3}):(#?[a-z0-9]+)")
    return {match[0]: match[1] for match in parser.findall(text.replace("\n", " "))}


def verify_document(document: dict) -> bool:
    valid_document = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    return valid_document.symmetric_difference(document.keys()) in [{"cid"}, set()]


def count_valid_documents(file_path: str) -> int:
    with open(file_path, "r") as file:
        return sum(verify_document(parse_credentials(document)) for document in file.read().split("\n\n"))


def main() -> None:
    answer = count_valid_documents("day_04_input.txt")
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
