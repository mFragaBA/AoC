def rucksack(ruck_as_string):
    return set(ruck_as_string)

with open('input.txt', 'r') as infile:
    lines = [rucksack(line.split()[0]) for line in infile.read().splitlines()]

total_priorities = 0
# len(lines) must be a multiple of three
for i in range(0, len(lines), 3):
    shared_item = list(lines[i].intersection(lines[i+1]).intersection(lines[i+2]))[0]
    priority = ord(shared_item) - ord('a') + 1 + int(shared_item.isupper()) * 58
    total_priorities += priority

print(total_priorities)
