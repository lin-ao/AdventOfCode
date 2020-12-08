import re
from collections import defaultdict


def parse_rule(rule: str) -> dict[str, str]:
    outer_parser = re.compile(r"^([a-z ]+) bags contain ([a-z0-9 ,]+).\n$")
    outer_bag, inner_bags = outer_parser.match(rule).groups()
    inner_parser = re.compile(r"(\d+) ([a-z ]+) bag[s]?")
    rule_dict = {inner_bag[1]: outer_bag for inner_bag in inner_parser.findall(inner_bags)}
    return rule_dict


def load_input(file_path: str) -> dict[str, set]:
    rules_dict = defaultdict(set)
    with open(file_path, "r") as file:
        for line in file:
            for key, value in parse_rule(line).items():
                rules_dict[key].add(value)
    return rules_dict


def search_bags(target_colors: set, rules_dict: dict[str, set], bags=None) -> int:
    if bags is None:
        bags = set()
    if target_colors:
        to_search = set()
        for color in target_colors:
            to_search |= rules_dict[color]
            bags |= rules_dict[color]
        return search_bags(to_search, rules_dict, bags)
    else:
        return len(bags)


def main() -> None:
    rules_dict = load_input("day_07_input.txt")
    colors_to_be_searched = {"shiny gold"}
    answer = search_bags(colors_to_be_searched, rules_dict)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
