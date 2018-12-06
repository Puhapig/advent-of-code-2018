# https://adventofcode.com/2018/day/1

from collections import namedtuple

INPUT_FILE = 'input.txt'

Dupes = namedtuple('Dupes', ['has_double', 'has_triple'])


def get_dupes(text):
    counts = [text.count(char) for char in text]
    return Dupes(has_double=2 in counts,
                 has_triple=3 in counts)


with open(INPUT_FILE, 'r') as input:
    lines = input.read().splitlines()
    dupes = [get_dupes(line) for line in lines]

    double_count = len([dupe for dupe in dupes if dupe.has_double])
    triple_count = len([dupe for dupe in dupes if dupe.has_triple])
    answer = double_count * triple_count

    print(f'part 1 answer: {answer}')