with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()

max_calo = 0
current = 0
for i in range(len(lines)):
    if lines[i]:
        current += int(lines[i])
    else:
        max_calo = max(current, max_calo)
        current = 0

print(max_calo)
