with open('input.txt') as infile:
    measurements = [int(l.strip(' \n')) for l in infile.readlines()]

count = 0

for i in range(3, len(measurements)):
    if measurements[i] > measurements[i-3]: #increased
        count += 1

print(count)
