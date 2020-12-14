import re

def applyMask(mask, num):
    n = list(bin(num)[2:])
    n = ['0' for _ in range(36 - len(n))] + n
    return "".join([n[i] if mask[i] == 'X' else mask[i] for i in range(36)])


def simulate(code):
    mask = [0 for _ in range(36)]
    mem = {}

    for line in code:
        pattern = r'mask\s=\s([0-1X]+)|mem\[(\d+)\]\s=\s(\d+)'
        match = re.search(pattern, line)
        if line[:4] == 'mask':
            print(match.group(1))
            mask = match.group(1) 
        else:
            memPos = match.group(2)
            num = int(match.group(3))
            mem[memPos] = int(applyMask(mask, num), 2)

    return sum(mem.values())


with open('d14_input.txt', 'r') as infile:
    code = infile.read().splitlines()

    print(simulate(code))
