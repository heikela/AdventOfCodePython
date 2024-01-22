from common.inputs import get_input, get_test_snippet
from common.point import Point2D

class Schematic():
    """A representation of the schematic in the puzzle"""
    def __init__(self, lines):
        self._lines = lines
        self.elemnents_py_pos = {}
        self.elements = []
        self._parse(lines)

    class Element():
        """A single element in the schematic"""
        def __init__(self, schematic: 'Schematic', positions: list[Point2D]):
            self.positions = positions
            self._schematic = schematic

        def neighbours(self):
            """Returns the elements adjacent to this element"""
            neighbours = set()
            for pos in self._neighbour_positions():
                if pos in self._schematic.elemnents_py_pos:
                    neighbours.add(self._schematic.elemnents_py_pos[pos])
            return neighbours

        def _neighbour_positions(self):
            """Returns the positions adjacent to this element"""
            positions = set()
            for pos in self.positions:
                for neighbour in pos.neighbours():
                    if not neighbour in self.positions:
                        positions.add(neighbour)
            return positions

        def is_part_number(self):
            """Returns whether this element is a part number"""
            # return false in case this is a symbol and not a number
            return False

        def is_symbol(self):
            """Returns whether this element is a symbol"""
            return False

        def is_gear(self):
            """Returns whether this element is a gear"""
            return False

    class Number(Element):
        """A number in the schematic"""
        def __init__(
                self,
                schematic: 'Schematic',
                positions: list[Point2D],
                value: int):
            super().__init__(schematic, positions)
            self.value = value

        def is_part_number(self):
            """Returns whether this number is a part number"""
            return any(n.is_symbol() for n in self.neighbours())

        def __repr__(self):
            return f"Number({self.positions[0]}-{self.positions[-1]} : {self.value})"

    class Symbol(Element):
        """A symbol in the schematic"""
        def __init__(
                self,
                schematic: 'Schematic',
                positions: list[Point2D],
                symbol: str):
            super().__init__(schematic, positions)
            self.symbol = symbol

        def is_symbol(self):
            return True

        def is_gear(self):
            """Returns whether this symbol is a gear"""
            if self.symbol != '*':
                return False
            return len([n for n in self.neighbours()
                       if n.is_part_number()]) == 2

        def gear_ratio(self):
            """Returns the gear ratio of this gear"""
            if not self.is_gear():
                raise ValueError("Not a gear")
            gear_numbers = [n for n in self.neighbours() if n.is_part_number()]
            return gear_numbers[0].value * gear_numbers[1].value

        def __repr__(self):
            return f"Symbol({self.positions[0]} : {self.symbol})"

    def part_number_sum(self):
        """Returns the sum of all part numbers"""
        return sum(n.value for n in self.elements if n.is_part_number())

    def gear_ratio_sum(self):
        """Returns the sum of all gear ratios"""
        return sum(n.gear_ratio() for n in self.elements if n.is_gear())

    def _parse(self, lines):
        current_digits = []
        digit_positions = []
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char in "0123456789":
                    current_digits.append(char)
                    digit_positions.append(Point2D(x, y))
                else:
                    if current_digits:
                        value = int("".join(current_digits))
                        number = self.Number(self, digit_positions, value)
                        current_digits = []
                        digit_positions = []
                        self._add_element(number)
                    if char != '.':
                        symbol = self.Symbol(self, [Point2D(x, y)], char)
                        self._add_element(symbol)
            if current_digits:
                value = int("".join(current_digits))
                number = self.Number(self, digit_positions, value)
                current_digits = []
                digit_positions = []
                self._add_element(number)

    def _add_element(self, element):
        """Adds an element to the schematic"""
        for pos in element.positions:
            self.elemnents_py_pos[pos] = element
        self.elements.append(element)

def main():
    snippet = get_test_snippet(2023, 3, 0)
    example = Schematic(snippet)
    print(f"Part 1 example: {example.part_number_sum()}")
    print(f"Part 2 example: {example.gear_ratio_sum()}")
    input = get_input(2023, 3)
    problem = Schematic(input)
    print(f"Part 1: {problem.part_number_sum()}")
    print(f"Part 2: {problem.gear_ratio_sum()}")

if __name__ == '__main__':
    main()
