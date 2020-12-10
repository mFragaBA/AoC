
def numberOfWays(joltages, i, prev, D):
    if i == len(joltages):
        return 1
    elif i > len(joltages):
        return 0

    if prev in D[i]:
        return D[i][prev]

    D[i][prev] = numberOfWays(joltages, i+1, joltages[i], D)
    if i+1 < len(joltages) and joltages[i+1] - prev <= 3:
        D[i][prev] = D[i][prev] + numberOfWays(joltages, i+1, prev, D)

    return D[i][prev]
    

with open('d10_input.txt', 'r') as infile:
    joltages = sorted([int(l) for l in infile.readlines()])
    joltages = joltages
    print(numberOfWays(joltages, 0, 0, [{} for _ in range(len(joltages))]))
        
