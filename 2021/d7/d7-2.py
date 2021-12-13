def groupTowards(crabs, pos):
    totalCost = 0
    for crab in crabs:
        numSteps = abs(pos - crab)
        totalCost += (numSteps * (numSteps+1)) / 2

    return totalCost

with open('input.txt') as infile:
    lines = [l.strip(' \n') for l in infile.readlines()]

crabs = [int(x) for x in lines[0].split(',')]
maxPos = max(c for c in crabs)
minCost = min(groupTowards(crabs, i) for i in range(maxPos))

print(minCost)
