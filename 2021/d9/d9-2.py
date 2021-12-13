def neighbours(hm, i, j):
    nh = []
    if i-1 >= 0: nh.append((i-1, j))
    if i+1 < len(hm): nh.append((i+1, j))
    if j-1 >= 0: nh.append((i, j-1))
    if j+1 < len(hm[0]): nh.append((i, j+1))

    return nh

def isLowPoint(hm, i, j):
    for neigh in neighbours(hm, i, j):
        if hm[i][j] >= hm[neigh[0]][neigh[1]]:
            return False

    return True

def bfs_count(hm, i, j, visited):
    if i < 0 or j < 0 or i >= len(hm) or j >= len(hm[0]): return 0
    visited.add((i, j))
    
    count = 1
    for neigh in neighbours(hm, i, j):
        if neigh not in visited and hm[neigh[0]][neigh[1]] > hm[i][j] and hm[neigh[0]][neigh[1]] < 9:
            count += bfs_count(hm, neigh[0], neigh[1], visited)

    return count


with open('input.txt') as infile:
    lines = [l.strip(' \n') for l in infile.readlines()]

heightmap = [[int(c) for c in l] for l in lines]

print(heightmap)

low_points = []
for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        if isLowPoint(heightmap, i, j):
            low_points.append((i, j))

basins = []
for lp in low_points:
    visited = set()
    lp_basin = bfs_count(heightmap, lp[0], lp[1], visited)
    basins.append(lp_basin)

basins = sorted(basins)
print(basins)

print(basins[-1]*basins[-2]*basins[-3])
