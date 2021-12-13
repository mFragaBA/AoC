def flash(octopuses, i, j, flashed):
    if flashed[i][j]: return
    #print(str(i) + "," + str(j) + " flashed")
    flashed[i][j] = True
   
    for l in range(-1, 2, 1):
        for r in range(-1, 2, 1):
            if l == 0 and  r == 0: continue
            if i+l< 0 or j+r< 0 or i+l>= 10 or j+r>= 10: continue
            octopuses[i+l][j+r] += 1
            if octopuses[i+l][j+r] > 9:
                flash(octopuses, i+l, j+r, flashed)


def step(octopuses):
    flashed = [[False for _ in range(10)] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            octopuses[i][j] += 1

    for i in range(10):
        for j in range(10):
            if octopuses[i][j] > 9:
                flash(octopuses, i, j, flashed)

    for i in range(10):
        for j in range(10):
            if flashed[i][j]:
                octopuses[i][j] = 0


with open('input.txt') as infile:
    lines = [l.strip(' \n') for l in infile.readlines()]

octopuses = [[int(x) for x in line] for line in lines]

flashes = 0

#print("before any steps")
#for row in octopuses:
    #print(''.join([str(x) for x in row]))

for i in range(1, 100000):
    step(octopuses)
    if all(all(octopuses[i][j] == 0 for i in range(10)) for j in range(10)):
        print("iter: " + str(i))
        break
