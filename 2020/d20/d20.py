import functools

class ImageTile:

    def connect(self, candidate):
        if any(all(side[i] == candSide[i] for i in range(len(side))) for side in self.sides for candSide in candidate.sides):
            self.matchCount += 1

    def __init__(self, imgTileStr):
        print(imgTileStr)
        self.id = imgTileStr.splitlines()[0].split(' ')[1][:-1]
        tiles = [ [c for c in line] for line in imgTileStr.splitlines()[1:]]

        self.sides = []
        top = tiles[0]
        bottom = tiles[-1]
        left = [tiles[i][0] for i in range(len(tiles))]
        right = [tiles[i][-1] for i in range(len(tiles))]
        self.sides.append(top)
        self.sides.append(list(reversed(top)))
        self.sides.append(bottom)
        self.sides.append(list(reversed(bottom)))
        self.sides.append(left)
        self.sides.append(list(reversed(left)))
        self.sides.append(right)
        self.sides.append(list(reversed(right)))
        self.matchCount = 0

with open('d20_input.txt', 'r') as infile:
    imageTiles = [ImageTile(t) for t in infile.read().strip().split('\n\n')]

    for i in range(len(imageTiles)):
        for j in range(len(imageTiles)):
            if i == j: continue
            imageTiles[i].connect(imageTiles[j])

    print([t.id for t in imageTiles])
    for a in imageTiles:
        print(a.matchCount)

    corners = [int(it.id) for it in imageTiles if it.matchCount == 2]
    print(functools.reduce(lambda a, b: a * b, corners))

