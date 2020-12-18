def neighbours(coord):
    return [(coord[0] + x, coord[1] + y, coord[2] + z) for z in range(-1, 2) for y in range(-1, 2) for x in range(-1, 2) if x != 0 or y != 0 or z != 0]

def candidateCubesFrom(activeCubes):
    candidates = set()
    for cube in activeCubes:
        for neigh in neighbours(cube):
            if neigh not in activeCubes:
                candidates.add(neigh)
    return candidates

def updateNewActivesFrom(candidates, currentActive, activatingValues, newActive):
    for cube in candidates:
        activeNeighbours = sum(1 if neigh in currentActive else 0 for neigh in neighbours(cube))
        
        if activeNeighbours in activatingValues:
            newActive.add(cube)


with open('d17_input.txt', 'r') as infile: 
    lines = infile.read().splitlines()
    activeCubes = set((x, y, 0) for x in range(len(lines)) for y in range(len(lines[x])) if lines[x][y] == '#')
    candidateCubes = candidateCubesFrom(activeCubes)

    for _ in range(6):
        newActive = set()

        updateNewActivesFrom(activeCubes, activeCubes, [2, 3], newActive)
        updateNewActivesFrom(candidateCubes, activeCubes, [3], newActive)
        
        newCandidates = candidateCubesFrom(newActive)
        activeCubes = newActive.copy()
        candidateCubes = newCandidates.copy()

    print(len(activeCubes))


