with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()

calories = []
current = 0
for i in range(len(lines)):
    if lines[i]:
        current += int(lines[i])
    else:
        calories.append(current)
        current = 0

sorted_calories = (sorted(calories))
print(sorted_calories[-1] + sorted_calories[-2] + sorted_calories[-3])
