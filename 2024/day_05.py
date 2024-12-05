from collections import defaultdict


def load_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def parse_input(_input: str) -> tuple[defaultdict[int, list[int]], list[list[int]]]:
    input_one, input_two = _input.split('\n\n')
    printing_rules = defaultdict(list)
    for rule in input_one.strip().split('\n'):
        rule = tuple(map(int, rule.split('|')))
        printing_rules[rule[1]].append(rule[0])
    page_orders = [[int(x) for x in order.strip().split(',')] for order in input_two.strip().split('\n')]
    return printing_rules, page_orders


def check_printing_validity(printing_rules: defaultdict[int, list[int]], page_order: list[int]) -> bool:
    for i, page in enumerate(page_order):
        for page_after in page_order[i:]:
            if page_after in printing_rules[page]:
                return False
    return True


def get_valid_page_orders(printing_rules: defaultdict[int, list[int]], page_orders: list[list[int]]) -> list[list[int]]:
    return [page_order for page_order in page_orders if check_printing_validity(printing_rules=printing_rules, page_order=page_order)]


def get_invalid_page_orders(printing_rules: defaultdict[int, list[int]], page_orders: list[list[int]]) -> list[list[int]]:
    return [page_order for page_order in page_orders if not check_printing_validity(printing_rules=printing_rules, page_order=page_order)]


def fix_page_order(printing_rules: defaultdict[int, list[int]], page_order: list[int]) -> list[int]:
    for i, page in enumerate(page_order):
        if page in printing_rules:
            for j in range(len(page_order) - 1, i, -1):
                if page_order[j] in printing_rules[page]:
                    page_order.pop(i)
                    page_order.insert(j, page)
                    return fix_page_order(printing_rules=printing_rules, page_order=page_order)
    return page_order


def count_page_numbers(valid_page_orders: list[list[int]]) -> int:
    page_number_sum = 0
    for valid_page_order in valid_page_orders:
        page_number_sum += valid_page_order[len(valid_page_order) // 2]
    return page_number_sum


def main() -> None:
    test_data: str = """
        47|53
        97|13
        97|61
        97|47
        75|29
        61|13
        75|53
        29|13
        97|29
        53|29
        61|53
        97|53
        61|29
        47|13
        75|47
        97|75
        47|61
        75|61
        47|29
        75|13
        53|13

        75,47,61,53,29
        97,61,53,29,13
        75,29,13
        75,97,47,61,53
        61,13,29
        97,13,75,29,47
    """
    test_printing_rules, test_page_orders = parse_input(_input=test_data)
    assert count_page_numbers(valid_page_orders=get_valid_page_orders(printing_rules=test_printing_rules, page_orders=test_page_orders))
    assert count_page_numbers(
        valid_page_orders=[
            fix_page_order(printing_rules=test_printing_rules, page_order=page_order) 
            for page_order
            in get_invalid_page_orders(printing_rules=test_printing_rules, page_orders=test_page_orders)
        ]
    ) == 123
    printing_rules, page_orders = parse_input(_input=load_input(filename="day_05_input.txt"))
    answer_part_one = count_page_numbers(valid_page_orders=get_valid_page_orders(printing_rules=printing_rules, page_orders=page_orders))
    answer_part_two = count_page_numbers(
        valid_page_orders=[
            fix_page_order(printing_rules=printing_rules, page_order=page_order) 
            for page_order
            in get_invalid_page_orders(printing_rules=printing_rules, page_orders=page_orders)
        ]
    ) 
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()
