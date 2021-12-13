def neighbours(hm, i, j):
    nh = []
    if i-1 >= 0: nh.append(hm[i-1][j])
    if i+1 < len(hm): nh.append(hm[i+1][j])
    if j-1 >= 0: nh.append(hm[i][j-1])
    if j+1 < len(hm[0]): nh.append(hm[i][j+1])

    return nh

def isLowPoint(hm, i, j):
    for neigh in neighbours(hm, i, j):
        if hm[i][j] >= neigh:
            return False

    return True

with open('input.txt') as infile:
    lines = [l.strip(' \n') for l in infile.readlines()]

heightmap = [[int(c) for c in l] for l in lines]

print(heightmap)

risk_sum = 0
for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        if isLowPoint(heightmap, i, j):
            print(str(i) + "," + str(j) + " is low point")
            risk_sum += heightmap[i][j] + 1

print(risk_sum)
