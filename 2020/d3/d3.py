import re


with open('d3_input.txt', 'r') as infile:
    lines = infile.read().splitlines()

    nrows = len(lines)
    ncols = len(lines[0])

    hSlope = 3
    vSlope = 1

    pos = [0, 0]
    treeCount = 0
    
    while pos[0] < nrows:
        if lines[pos[0]][pos[1]] == '#':
            treeCount = treeCount + 1
        
        pos[0] = pos[0] + vSlope
        pos[1] = (pos[1] + hSlope) % ncols

    print(treeCount)

        
