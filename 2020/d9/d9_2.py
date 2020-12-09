
def hasTwoThatAddUpTo(previousNums, value):
    for num in previousNums:
        for anotherNum in previousNums:
            if num != anotherNum and num + anotherNum == value:
                return True

    return False

with open('d9_input.txt', 'r') as infile:
    lines = infile.read().splitlines()
    lines = [int(line) for line in lines]
    fifoQueue = [num for num in lines[:25]]

    idx = 25
    while idx < len(lines) and hasTwoThatAddUpTo(fifoQueue, lines[idx]):
        fifoQueue.append(lines[idx])
        fifoQueue.pop(0)
        idx = idx + 1

    target = lines[idx]

    for i in range(len(lines)):
        for j in range(i+2, len(lines)):
            if sum(lines[i:j]) == target:
                print(min(lines[i:j]) + max(lines[i:j]))
