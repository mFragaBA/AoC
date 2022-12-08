import re


def intervals(line):
    match = re.match(r"(\d+)\-(\d+),(\d+)-(\d+)", line)
    return [[int(match.group(1)), int(match.group(2))], [int(match.group(3)), int(match.group(4))]]

def fully_contains(i1, i2):
    return i1[0] <= i2[0] and i1[1] >= i2[1]

with open('input.txt', 'r') as infile:
    lines = [intervals(line) for line in infile.read().splitlines()]


count = 0
for intervals in lines:
    if fully_contains(intervals[0], intervals[1]) or fully_contains(intervals[1], intervals[0]):
        count += 1

print(count)
