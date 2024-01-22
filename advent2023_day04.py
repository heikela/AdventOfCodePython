from common.inputs import get_input, get_test_snippet
from collections import namedtuple

Card = namedtuple("Card", ["index", "correct", "numbers"])

def parse_cards(lines):
    """Parse the cards from the input"""
    cards = []
    for line in lines:
        title, numbers = line.split(":")
        index = int(title.split()[1])
        correct_part, actual_part = numbers.split("|")
        correct = [int(n) for n in correct_part.strip().split()]
        actual = [int(n) for n in actual_part.strip().split()]
        card = Card(index, correct, actual)
        cards.append(card)
    return cards

def count_correct(card: Card):
    """Count correct numbers in a card"""
    return len(set(card.numbers) & set(card.correct))

def card_points(card: Card):
    """Return the points for the card in part 1"""
    result = 0
    for i in range(count_correct(card)):
        if result == 0:
            result = 1
        else:
            result *= 2
    return result

def part1(input: list[str]):
    """Solve part 1"""
    cards = parse_cards(input)
    return sum(card_points(card) for card in cards)

def main():
    """Main entry point"""
    print(f"part 1 example: {part1(get_test_snippet(2023, 4, 0))}")
    print(f"part 1: {part1(get_input(2023, 4))}")

if __name__ == "__main__":
    main()
