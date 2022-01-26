from collections import defaultdict
from math import prod

from day_16_part_1 import load_input, parse_rules, parse_tickets, is_valid


def parse_my_ticket(ticket: str) -> tuple[int]:
    return tuple(map(int, ticket.rstrip("\n").split("\n")[1].split(",")))


def check_tickets(tickets: list[tuple[int]], bounds: list[tuple[int]]) -> list[tuple[int]]:
    return [ticket for ticket in tickets if all(any(is_valid(value, bound) for bound in bounds) for value in ticket)]


def assign_fields(valid_tickets: list[tuple[int]], bounds: list[tuple[int]]) -> dict[int, int]:
    possible_indexes = defaultdict(list)
    final_indexes = {}
    tickets_transformed = list(zip(*valid_tickets))
    # Finding all possible values for each ticket field
    for bound in bounds:
        for field in tickets_transformed:
            if all(is_valid(value, bound) for value in field):
                possible_indexes[bounds.index(bound)].append(tickets_transformed.index(field))
    # Iteratively reducing the possible values for each field until each field only has one possible value
    while any(len(item) > 1 for item in possible_indexes.values()):
        for possible in possible_indexes:
            if len(possible_indexes[possible]) == 1:
                final_indexes[possible] = possible_indexes[possible][0]
        for final in final_indexes.values():
            for possible in possible_indexes:
                if final in possible_indexes[possible]:
                    possible_indexes[possible].remove(final)
    for possible in possible_indexes:
        if len(possible_indexes[possible]) == 1:
            final_indexes[possible] = possible_indexes[possible][0]
    return final_indexes


def main() -> None:
    rules, my_ticket, nearby_tickets = load_input("day_16_input.txt")
    bounds = parse_rules(rules)
    tickets = parse_tickets(nearby_tickets)
    valid_tickets = check_tickets(tickets, bounds)
    my_ticket = parse_my_ticket(my_ticket)
    indexes = assign_fields(valid_tickets, bounds)
    answer = prod(my_ticket[indexes[i]] for i in range(0, 6))
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
