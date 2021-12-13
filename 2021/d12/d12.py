G = {}

def isBig(neigh):
    return neigh.isupper()

def numPaths(source, to, is_visited):
    if is_visited[source] and not isBig(source): return 0
    if source == to: return 1
    is_visited[source] = True

    total_paths = 0
    for neigh in G[source]:
        total_paths += numPaths(neigh, to, is_visited)
    
    is_visited[source] = False

    return total_paths

with open('input.txt') as infile:
    lines = [l.strip(' \n') for l in infile.readlines()]


for line in lines:
    nodes = line.split('-')
    if nodes[0] not in G:
        G[nodes[0]] = []
    G[nodes[0]].append(nodes[1])

    if nodes[1] not in G:
        G[nodes[1]] = []
    G[nodes[1]].append(nodes[0])

visited = {}
for key in G:
    visited[key] = False

print(numPaths('start', 'end', visited))

