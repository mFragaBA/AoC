
FLOOR = '.'
EMPTYSEAT = 'L'
OCCUPIEDSEAT = '#'

def countOccupied(layout, i, j):
    occupied = 0
    for l in range(-1, 2):
        for r in range(-1, 2):
            if l == 0 and r == 0:
                continue
            occupied += int(layout[i-l][j-r] == OCCUPIEDSEAT)

    return occupied

with open('d11_input.txt', 'r') as infile:
    lines = infile.read().splitlines()
    seatLayout = [['.' for _ in range(len(lines[0]) + 2)]]
    seatLayout = seatLayout + ['.' + line + '.' for line in lines]
    seatLayout = seatLayout + [['.' for _ in range(len(lines[0]) + 2)]]


    newLayout = [['.' for seat in row] for row in seatLayout]
    while True:
        newLayout = [['.' for seat in row] for row in seatLayout]
        for i in range(1, len(seatLayout) - 1):
            for j in range(1, len(seatLayout[i]) - 1):
                occupied = countOccupied(seatLayout, i, j)
                if seatLayout[i][j] == EMPTYSEAT and occupied == 0:
                    newLayout[i][j] = OCCUPIEDSEAT
                elif seatLayout[i][j] == OCCUPIEDSEAT and occupied >= 4:
                    newLayout[i][j] = EMPTYSEAT
                else:
                    newLayout[i][j] = seatLayout[i][j]

        if (all(seatLayout[i][j] == newLayout[i][j] for i in range(len(seatLayout)) for j in range(len(seatLayout[0])))):
            break

        seatLayout = [[v for v in row] for row in newLayout]

        for row in seatLayout:
            print("".join(row))
        print("")


    occupiedCount = 0
    for row in newLayout:
        for seat in row:
            occupiedCount += int(seat == OCCUPIEDSEAT)

    print(occupiedCount)




