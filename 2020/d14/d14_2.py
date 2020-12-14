import re

def applyMask(mask, num):
    n = bin(num)[2:]
    n = n.zfill(36) 
    return ['X' if mask[i] == 'X' else str(int(bool(int(mask[i])) or bool(int(n[i])))) for i in range(36)]


def simulate(code):
    mask = [0 for _ in range(36)]
    mem = {}

    for line in code:
        pattern = r'mask\s=\s([0-1X]+)|mem\[(\d+)\]\s=\s(\d+)'
        match = re.search(pattern, line)
        if line[:4] == 'mask':
            mask = match.group(1) 
        else:
            memPos = int(match.group(2))
            num = int(match.group(3))
           
            decodedPos = applyMask(mask, memPos)
            xCount = sum(int(x == 'X') for x in decodedPos)
            for bitConfig in [bin(i)[2:].zfill(xCount) for i in range(2 ** xCount)]:
                viablePos = [ p for p in decodedPos ]
                for bit in bitConfig:
                    viablePos[viablePos.index('X')] = bit

                memPos = "".join(viablePos)
                mem[int(memPos, 2)] = num

    return sum(mem.values())


with open('d14_input.txt', 'r') as infile:
    code = infile.read().splitlines()

    print(simulate(code))
