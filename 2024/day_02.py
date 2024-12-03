def load_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def parse_input(_input: str) -> list[list[int]]:
    return [[int(level) for level in report.strip().split(" ")] for report in _input.strip().split("\n")]


def check_report_safety(report: list[int]) -> bool:
    if report != sorted(report, reverse=True) and report != sorted(report, reverse=False):
        return False
    elif len(report) != len(set(report)):
        return False
    else:
        report_is_valid = True
        for idx, level in enumerate(report):
            if idx + 1 == len(report):
                break
            if abs(report[idx + 1] - level) > 3:
                report_is_valid = False
                break
        return report_is_valid


def check_report_safety_with_dampener(report: list[int]) -> bool:
    if check_report_safety(report):
        return True
    else:
        for i in range(len(report)):
            if check_report_safety(report[:i] + report[i + 1 :]):
                return True
        return False


def count_safe_reports(reports: list[list[int]], with_dampener: bool = False) -> int:
    if with_dampener:
        return sum(map(check_report_safety_with_dampener, reports))
    else:
        return sum(map(check_report_safety, reports))


def main() -> None:
    test_data: list[list[int]] = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert count_safe_reports(reports=test_data) == 2
    assert count_safe_reports(reports=test_data, with_dampener=True) == 4
    reports = parse_input(_input=load_input(filename="day_02_input.txt"))
    answer_part_one = count_safe_reports(reports=reports)
    answer_part_two = count_safe_reports(reports=reports, with_dampener=True)
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()
