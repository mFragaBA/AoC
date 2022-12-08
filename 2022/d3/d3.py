def rucksack(ruck_as_string):
    mid = len(ruck_as_string) // 2
    return [set(ruck_as_string[:mid]), set(ruck_as_string[mid:])]

with open('input.txt', 'r') as infile:
    lines = [rucksack(line.split()[0]) for line in infile.read().splitlines()]

total_priorities = 0
for rsk in lines:
    shared_item = list(rsk[0].intersection(rsk[1]))[0]
    priority = ord(shared_item) - ord('a') + 1 + int(shared_item.isupper()) * 58
    total_priorities += priority

print(total_priorities)
