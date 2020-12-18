
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

movements = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}

antiClockwiseRotations = [
    [[1, 0], [0, 1]],
    [[0, -1], [1, 0]],
    [[-1, 0], [0, -1]],
    [[0, 1], [-1, 0]],

]

def mult(M, v):
    return [M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1]]

with open('d12_input.txt', 'r') as infile:
    lines = [(l[0], int(l[1:])) for l in infile.read().splitlines()]

    pos = [0, 0]
    waypointPos = [10, 1]

    for op in lines:
        if op[0] in movements:
            waypointPos[0] += dirs[movements[op[0]]][0] * op[1]
            waypointPos[1] += dirs[movements[op[0]]][1] * op[1]
        elif op[0] == 'F':
            posToWaypoint = [waypointPos[0] - pos[0], waypointPos[1] - pos[1]]
            pos[0] += posToWaypoint[0] * op[1]
            pos[1] += posToWaypoint[1] * op[1]
            waypointPos[0] += posToWaypoint[0] * op[1]
            waypointPos[1] += posToWaypoint[1] * op[1]
        else: 
            dirShift = (op[1] // 90) % 4
            if op[0] == 'R' and dirShift != 2:
                dirShift = (dirShift + 2) % 4

            centeredWaypoint = [waypointPos[0] - pos[0], waypointPos[1] - pos[1]]
            waypointPos = mult(antiClockwiseRotations[dirShift], centeredWaypoint)
            waypointPos = [waypointPos[0] + pos[0], waypointPos[1] + pos[1]]

    print(str(abs(pos[0]) + abs(pos[1])))

