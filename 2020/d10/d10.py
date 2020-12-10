

with open('d10_input.txt', 'r') as infile:
    joltages = sorted([int(l) for l in infile.readlines()])
    prev = 0
    threeDiffCount = 0
    oneDiffCount = 0
    for i, joltage in enumerate(joltages):
        if joltage - prev == 1:
            oneDiffCount += 1
        elif joltage - prev == 3:
            threeDiffCount += 1

        prev = joltage

    threeDiffCount += 1
    print(oneDiffCount * threeDiffCount)
        
