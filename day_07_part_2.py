import re
from collections import defaultdict


def parse_rule(rule: str) -> dict[str, dict[str, int]]:
    rule_dict = defaultdict(dict)
    outer_parser = re.compile(r"^([a-z ]+) bags contain ([a-z0-9 ,]+).\n$")
    outer_bag, inner_bags = outer_parser.match(rule).groups()
    inner_parser = re.compile(r"(\d+) ([a-z ]+) bag[s]?")
    for inner_bag in inner_parser.findall(inner_bags):
        rule_dict[outer_bag].update({inner_bag[1]: int(inner_bag[0])})
    return rule_dict


def load_input(file_path: str) -> dict[str, dict[str, int]]:
    rules_dict = defaultdict(dict)
    with open(file_path, "r") as file:
        for line in file:
            for key, value in parse_rule(line).items():
                rules_dict[key] |= value
    return rules_dict


def search_bags(target_colors: dict, rules_dict: dict, bags=0) -> int:
    if target_colors:
        to_search = defaultdict(lambda: 0)
        contain_bag = set(target_colors.keys()).intersection(rules_dict.keys())
        do_not_contain_bags = target_colors.keys() - contain_bag
        for color in contain_bag:
            bags += target_colors[color]
            for item in rules_dict[color].items():
                to_search[item[0]] += target_colors[color] * item[1]
        for color in do_not_contain_bags:
            bags += target_colors[color]
        return search_bags(to_search, rules_dict, bags)
    else:
        return bags - 1


def main() -> None:
    rules_dict = load_input("day_07_input.txt")
    colors_to_be_searched = {"shiny gold": 1}
    answer = search_bags(colors_to_be_searched, rules_dict)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
