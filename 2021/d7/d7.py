def groupTowards(crabs, pos):
    totalCost = 0
    for crab in crabs:
        totalCost += abs(crabs[pos] - crab)

    return totalCost

with open('input.txt') as infile:
    lines = [l.strip(' \n') for l in infile.readlines()]

crabs = [int(x) for x in lines[0].split(',')]
minCost = min(groupTowards(crabs, i) for i in range(len(crabs)))

print(minCost)
