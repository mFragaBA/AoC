
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

movements = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}

with open('d12_input.txt', 'r') as infile:
    lines = [(l[0], int(l[1:])) for l in infile.read().splitlines()]

    pos = [0, 0]
    direction = 1

    for op in lines:
        if op[0] in movements:
            pos[0] += dirs[movements[op[0]]][0] * op[1]
            pos[1] += dirs[movements[op[0]]][1] * op[1]
        elif op[0] == 'F':
            pos[0] += dirs[direction][0] * op[1]
            pos[1] += dirs[direction][1] * op[1]
        elif op[0] == 'L':
            dirShift = (op[1] // 90) % 4
            direction = (direction + 4 - dirShift) % 4
        elif op[0] == 'R':
            dirShift = (op[1] // 90) % 4
            direction = (direction + dirShift) % 4
        else:
            print('ERROR: parsing done wrong')

    print(str(abs(pos[0]) + abs(pos[1])))

