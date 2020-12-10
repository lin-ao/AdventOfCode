from day_01_part_1 import load_input


def find_jolt_differences(adapters: list[int]) -> int:
    differences = []
    prev = 0
    for adapter in adapters:
        differences.append(adapter - prev)
        prev = adapter
    return differences.count(1) * differences.count(3)


def main() -> None:
    adapters = sorted(load_input("day_10_input.txt"))
    adapters.append(max(adapters) + 3)
    answer = find_jolt_differences(adapters)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
