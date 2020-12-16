import re


def load_input(file_path: str) -> tuple[str, str, str]:
    with open(file_path, "r") as file:
        rules, my_ticket, tickets = file.read().split("\n\n")
        return rules, my_ticket, tickets


def parse_rules(rules: str) -> list[tuple[int]]:
    parser = re.compile(r"^[a-z ]+: (\d+)-(\d+) or (\d+)-(\d+)")
    bounds = [tuple(map(int, parser.findall(rule)[0])) for rule in rules.split("\n")]
    return bounds


def parse_tickets(tickets: str) -> list[tuple[int]]:
    values = [tuple(map(int, ticket.split(",")))for ticket in tickets.rstrip("\n").split("\n")[1:]]
    return values


def is_valid(value: int, bound: tuple[int]) -> bool:
    return bound[0] <= value <= bound[1] or bound[2] <= value <= bound[3]


def check_values(tickets: list[tuple[int]], bounds: list[tuple[int]]) -> int:
    return sum(value for ticket in tickets for value in ticket if not any(is_valid(value, bound) for bound in bounds))


def main() -> None:
    rules, my_ticket, nearby_tickets = load_input("day_16_input.txt")
    bounds = parse_rules(rules)
    tickets = parse_tickets(nearby_tickets)
    answer = check_values(tickets, bounds)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
