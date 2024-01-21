from common.inputs import get_input
from collections import ChainMap
from typing import Dict

digits = {str(i) : i for i in range(10)}

spelled_digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four' : 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

all_digits = ChainMap(digits, spelled_digits)

def contains_at_pos(line: str, pos: int, sub_string: str) -> bool:
    return line[pos:].startswith(sub_string)

def first_digit(line: str, digits: Dict[str, int]) -> int:
    for i in range(len(line)):
        for digit_representation, value in digits.items():
            if contains_at_pos(line, i, digit_representation):
                return value
    raise ValueError("No digit found in line")

def last_digit(line: str, digits: Dict[str, int]) -> int:
    for i in range(len(line) - 1, -1, -1):
        for digit_representation, value in digits.items():
            if contains_at_pos(line, i, digit_representation):
                return value
    raise ValueError("No digit found in line")

def line_to_number(line: str, digits: Dict[str, int]) -> int:
    return 10 * first_digit(line, digits) + last_digit(line, digits)

def main():
    input = get_input(2023, 1)
    part1 = sum(line_to_number(line, digits) for line in input)
    print("part 1: %d" % part1)
    part2 = sum(line_to_number(line, all_digits) for line in input)
    print("part 2: %d" % part2)

if __name__ == '__main__':
    main()
