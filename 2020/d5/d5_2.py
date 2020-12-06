import re

def seatId(row, col):
    return 8 * row + col

def buildSeatId(seatStr):
    row = int(''.join(('1' if x == 'B' else '0') for x in seatStr[:7]), 2)
    col = int(''.join(('1' if x == 'R' else '0') for x in seatStr[7:]), 2)
    return seatId(row, col)

def lastRow(sId):
    return sId >= 8 * 127

def firstRow(sId):
    return sId < 8

with open('d5_input.txt', 'r') as infile:
    lines = infile.read().splitlines()

    seatIds = list(map(lambda seatStr: buildSeatId(seatStr), lines))
    for sId in seatIds:
        if lastRow(sId) or firstRow(sId): continue
        if (sId + 2) in seatIds and not (sId + 1) in seatIds:
            print(sId + 1)
        elif (sId - 2) in seatIds and not (sId - 1) in seatIds:
            print(sId - 1)
