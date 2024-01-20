import common.inputs
from collections import namedtuple, Counter

Game = namedtuple('Game', ['id', 'counts'])

def parse_line(line: str) -> Game:
    parts = line.split(':')
    id = int(parts[0].split()[1])
    counts = Counter()
    for sample in parts[1].split(';'):
        for colour_sample in sample.strip().split(','):
            num, colour = colour_sample.strip().split()
            sample_counter = Counter()
            sample_counter[colour] = int(num)
            counts = counts | sample_counter
    return Game(id, counts)

part1_bag = Counter(red=12, green=13, blue=14)

def is_valid_part1(game: Game) -> bool:
    return game.counts <= part1_bag

def power(game: Game) -> int:
    return game.counts['red'] * game.counts['green'] * game.counts['blue']

def main():
    input = common.inputs.get_input(2023, 2)
    games = [parse_line(line) for line in input]
    part1 = sum(game.id for game in games if is_valid_part1(game))
    print("part 1: %d" % part1)
    part2 = sum(power(game) for game in games)
    print("part 2: %d" % part2)

if __name__ == '__main__':
    main()
