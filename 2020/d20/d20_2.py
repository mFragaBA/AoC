import functools

def transformBoard(board, rotate, flipX, flipY):
    width = len(board)
    height = len(board[0])
    tiles = [['' for _ in range(width if rotate else height)] for _ in range(height if rotate else width)]
    for i in range(height if rotate else width):
        for j in range(width if rotate else height):
            if rotate:
                tiles[i][j] = board[j if not flipX else width - 1 - j][i if flipY else height - 1 - i]
            else:
                tiles[i][j] = board[i if not flipX else width - 1 - i][j if not flipY else height - 1 - j]
    return tiles


class ImageTile:

    def checkConnection(oneIt, anotherIt):
        size = len(anotherIt.tiles)
        if all(oneIt.tiles[0][i] == anotherIt.tiles[size - 1][i] for i in range(size)):
            oneIt.above = anotherIt
            anotherIt.below = oneIt
            oneIt.matches.append(anotherIt.id)
            anotherIt.matches.append(oneIt.id)
            return True
        if all(oneIt.tiles[i][size - 1] == anotherIt.tiles[i][0] for i in range(size)):
            oneIt.right = anotherIt
            anotherIt.left = oneIt
            oneIt.matches.append(anotherIt.id)
            anotherIt.matches.append(oneIt.id)
            return True
        if all(oneIt.tiles[size - 1][i] == anotherIt.tiles[0][i] for i in range(size)):
            oneIt.below = anotherIt
            anotherIt.above = oneIt
            oneIt.matches.append(anotherIt.id)
            anotherIt.matches.append(oneIt.id)
            return True
        if all(oneIt.tiles[i][0] == anotherIt.tiles[i][size - 1] for i in range(size)):
            oneIt.left = anotherIt
            anotherIt.right = oneIt
            oneIt.matches.append(anotherIt.id)
            anotherIt.matches.append(oneIt.id)
            return True

        return False

    def adjustAndConnect(modifiableIt, staticIt):
        tilesCpy = [[c for c in row] for row in modifiableIt.tiles]
        for flipX in [True, False]:
            for flipY in [True, False]:
                for rotate in [True, False]:
                    modifiableIt.adjust(rotate, flipX, flipY)
                    if ImageTile.checkConnection(modifiableIt, staticIt):
                        return True
                    modifiableIt.tiles = [[c for c in row] for row in tilesCpy]

        return False


    def connect(self, candidate):
        if (candidate.id in self.matches):
            return True

        if len(candidate.matches) > 0 and len(self.matches) == 0:
            return ImageTile.adjustAndConnect(self, candidate)
        elif len(self.matches) > 0 and len(candidate.matches) == 0:
            return ImageTile.adjustAndConnect(candidate, self)
        
        return ImageTile.checkConnection(self, candidate)


    def adjust(self, rotate, flipX, flipY):
        self.tiles = [[c for c in row] for row in transformBoard(self.tiles, rotate, flipX, flipY)]
                    

    def __init__(self, imgTileStr):
        self.id = imgTileStr.splitlines()[0].split(' ')[1][:-1]
        self.tiles = [ [c for c in line] for line in imgTileStr.splitlines()[1:]]
        self.left = -1
        self.above = -1
        self.right = -1
        self.below = -1
        self.matches = []

def connectAll(imageTiles, i, connected):
    matches = []
    connected.append(i)
    for j in range(len(imageTiles)):
        if imageTiles[i].connect(imageTiles[j]):
            matches.append(j)
    
    for j in matches:
        match = imageTiles[j]
        if j not in connected:
           connectAll(imageTiles, j, connected) 

def fillBoardAt(i, j, board, it):
    for x in range(8):
        for y in range(8):
            board[i+x][j+y] = it.tiles[x+1][y+1]

def markSeaMonsters(board):
    seaMonster = [
            '                  # ',
            '#    ##    ##    ###',
            ' #  #  #  #  #  #   '
    ]
    seaMonster = [[c for c in row] for row in seaMonster]

    for flipX in [True, False]:
        for flipY in [True, False]:
            for rotate in [True, False]:
                transformedBoard = transformBoard(board, rotate, flipX, flipY)
                foundCount = 0
                for i in range(0, 12 * 8 - len(seaMonster)):
                    for j in range(0, 12 * 8 - len(seaMonster[0])):
                        found = True
                        for x in range(len(seaMonster)):
                            for y in range(len(seaMonster[0])):
                                if seaMonster[x][y] == '#' and transformedBoard[i+x][j+y] != '#' and transformedBoard[i+x][j+y] != 'O':
                                    found = False
                                    break
                            if not found:
                                break
                        if found:
                            foundCount += 1
                            for x in range(len(seaMonster)):
                                for y in range(len(seaMonster[0])):
                                    if seaMonster[x][y] == '#':
                                        transformedBoard[i+x][j+y] = 'O'
                if foundCount > 0:
                    return [ [c for c in row] for row in transformedBoard]


with open('d20_input.txt', 'r') as infile:
    imageTiles = [ImageTile(t) for t in infile.read().strip().split('\n\n')]

    connected = []
    for i in range(len(imageTiles)):
        if i not in connected:
            connectAll(imageTiles, i, connected)

    tl = [it for it in imageTiles if it.left == -1 and it.above == -1][0]

    board = [['' for _ in range(12 * 8)] for _ in range(12 * 8)]
    i = 0
    itRow = tl
    while itRow != -1:
        j = 0
        itCol = itRow
        while itCol != -1:
            fillBoardAt(i, j, board, itCol)
            itCol = itCol.right
            j += 8

        itRow = itRow.below
        i += 8



    board = markSeaMonsters(board)
    print(sum(int(board[i][j] == '#') for i in range(12 * 8) for j in range(12 * 8)))

