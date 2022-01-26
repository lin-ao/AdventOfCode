from math import inf
from typing import Union


def load_input(filename: str) -> list[str]:
    with open(filename) as f:
        return [(line.rstrip("\n")) for line in f]


def transpose_bits(binary_bits: list[str]) -> list[list[str]]:
    return [list(row) for row in zip(*list(binary_bits))]


def calculate_gamma(transposed_bits: list[list[str]]) -> int:
    return int("".join([max(set(transposed_bit), key=transposed_bit.count) for transposed_bit in transposed_bits]), 2)


def calculate_epsilon(transposed_bits: list[list[str]]) -> int:
    return int("".join([min(set(transposed_bit), key=transposed_bit.count) for transposed_bit in transposed_bits]), 2)


def update_bits(binary_bits: list[str], sig_digit: str) -> list[str]:
    return ["".join(list(binary_bit)[1:]) for binary_bit in binary_bits if binary_bit[0] == sig_digit]


def calculate_oxygen(binary_bits: list[str], transposed_bits: list[list[str]], result=None) -> int:
    if result is None:
        result: list[Union[str, None]] = []
    if transposed_bits:
        binary_bits: list[str] = binary_bits
        zero: int = transposed_bits[0].count("0")
        one: int = transposed_bits[0].count("1")
        sig_digit: int = "0" if zero > one else "1"
        result.append(sig_digit)
        updated_bits: list[str] = update_bits(binary_bits, sig_digit)
        updated_transposed_bits: list[list[str]] = transpose_bits(updated_bits)
        return calculate_oxygen(updated_bits, updated_transposed_bits, result)
    else:
        return int("".join(result), 2)


def calculate_co2(binary_bits: list[str], transposed_bits: list[list[str]], result=None) -> int:
    if result is None:
        result: list[Union[str, None]] = []
    if transposed_bits:
        binary_bits: list[str] = binary_bits
        zero: int = transposed_bits[0].count("0") if "0" in transposed_bits[0] else inf
        one: int = transposed_bits[0].count("1") if "1" in transposed_bits[0] else inf
        sig_digit: int = "1" if one < zero else "0"
        result.append(sig_digit)
        updated_bits: list[str] = update_bits(binary_bits, sig_digit)
        updated_transposed_bits: list[list[str]] = transpose_bits(updated_bits)
        return calculate_co2(updated_bits, updated_transposed_bits, result)
    else:
        return int("".join(result), 2)


def main() -> None:
    test_data: list[str] = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    assert calculate_gamma(transpose_bits(test_data)) == 22
    assert calculate_epsilon(transpose_bits(test_data)) == 9
    assert calculate_oxygen(test_data, transpose_bits(test_data)) == 23
    assert calculate_co2(test_data, transpose_bits(test_data)) == 10

    binary_bits: list[str] = load_input("day_03_input.txt")
    transposed_bits: list[list[str]] = transpose_bits(binary_bits)
    gamma: int = calculate_gamma(transposed_bits)
    epsilon: int = calculate_epsilon(transposed_bits)
    oxygen: int = calculate_oxygen(binary_bits, transposed_bits)
    co2: int = calculate_co2(binary_bits, transposed_bits)

    answer_part_one: int = gamma * epsilon
    answer_part_two: int = oxygen * co2
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()