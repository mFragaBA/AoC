import re

def seatId(row, col):
    return 8 * row + col

with open('d5_input.txt', 'r') as infile:
    lines = infile.read().splitlines()

    maxId = 0;
    for line in lines:
        row = int(''.join(('1' if x == 'B' else '0') for x in line[:7]), 2)
        col = int(''.join(('1' if x == 'R' else '0') for x in line[7:]), 2)
        maxId = max(maxId, seatId(row, col))

    print(maxId)


        
