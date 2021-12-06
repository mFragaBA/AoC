# (x1, y1) -> (x2, y2) => t * (x2-x1, y2-y1) + (x1, y1)
# t * (x2-x1, y2-y1) + (x1, y1) = (x3, y3) if
# t * (x2-x1, y2-y1) = (x3 - x1, y3 - y1)
# t = (x3-x1, y3-y1) / (x2-x1, y2-y1)
# and y is in [0, 1 range]
# 2 4 - 3 4 1 4
def same(a, b):
    return abs(a - b) < 0.000001

def covers(x, y, line):
    if line[0][0] != line[1][0]:
        t = float((x - line[0][0]))/(line[1][0] - line[0][0])
    else:
        t = float((y - line[0][1]))/(line[1][1] - line[0][1])


    return 0.0 <= t and t <= 1.0 and same(t * (line[1][0] - line[0][0]) + line[0][0], x) and same(t * (line[1][1] - line[0][1]) + line[0][1], y)
    

def numCovering(x, y, lines):
    count = 0
    for line in lines:
        if covers(x, y, line):
            count += 1

    return count

with open('input.txt') as infile:
    inp = [l.strip(' \n').split('->') for l in infile.readlines()]

lines = []
for l in inp:
    f = [int(x) for x in l[0].strip().split(',')]
    t = [int(x) for x in l[1].strip().split(',')]

    # considering horizontal or vertical for now
    lines.append((f, t))

#print(lines)

maxX = lines[0][0][0]
maxY = lines[0][0][1]

for line in lines:
    maxX = max(maxX, max(line[0][0], line[1][0]))
    maxY = max(maxY, max(line[0][1], line[1][1]))

print(maxX)
print(maxY)
overlapped = 0
#board = [['.' for _ in range(maxY+1)] for _ in range(maxX+1)]

for x in range(0, maxX+1):
    for y in range(0, maxY+1):
        #print('{},{}'.format(x, y))
        nc = numCovering(x, y, lines)
        #board[y][x] = str(nc)
        if nc >= 2:
            overlapped += 1

print(overlapped)
#print('\n'.join([''.join(l) for l in board]))
