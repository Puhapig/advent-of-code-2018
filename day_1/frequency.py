# https://adventofcode.com/2018/day/1

INPUT_FILE = 'input.txt'

# part 1
with open(INPUT_FILE, 'r') as input:
    answer = sum([int(line) for line in input.readlines()])
    print(f'part 1 answer: {answer}')



# part 2
def find_repeated_frequency(lines):
    total = 0
    seen = {0: True}

    while True:
        for value in lines:
            total += value
            if total in seen: return total
            seen[total] = True

with open(INPUT_FILE, 'r') as input:
    lines = [int(line) for line in input.readlines()]
    answer = find_repeated_frequency(lines)
    print(f'part 2 answer: {answer}')