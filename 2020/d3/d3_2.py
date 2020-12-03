
def countTreesWithSlope(treeLayout, slope):
    nrows = len(treeLayout)
    ncols = len(treeLayout[0])

    hSlope = slope[0]
    vSlope = slope[1]

    pos = [0, 0]
    treeCount = 0
    
    while pos[0] < nrows:
        if lines[pos[0]][pos[1]] == '#':
            treeCount = treeCount + 1
        
        pos[0] = pos[0] + vSlope
        pos[1] = (pos[1] + hSlope) % ncols

    return treeCount


with open('d3_input.txt', 'r') as infile:
    lines = infile.read().splitlines()

    slopes = list(map(lambda x: countTreesWithSlope(lines, x), [[1,1], [3, 1], [5, 1], [7, 1], [1, 2]]))
    print(slopes)
    print(slopes[0] * slopes[1] * slopes[2] * slopes[3] * slopes[4])

        
