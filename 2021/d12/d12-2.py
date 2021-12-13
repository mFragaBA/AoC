G = {}

def isBig(neigh):
    return neigh.isupper()

paths = []
def numPaths(source, to, visit_count, double_visit_done, path):
    if (visit_count[source] >=2 or (visit_count[source] == 1 and double_visit_done)) and not isBig(source): return 0
    if visit_count['start'] == 2 or visit_count['end'] == 2: return 0
    if source == to:
        path.append(to)
        paths.append([x for x in path])
        path.pop()
        return 1

    visit_count[source] += 1
    path.append(source)
    if visit_count[source] == 2 and not isBig(source): double_visit_done = True

    total_paths = 0
    for neigh in G[source]:
        total_paths += numPaths(neigh, to, visit_count, double_visit_done, path)
    
    if visit_count[source] == 2 and not isBig(source): double_visit_done = False
    path.pop()
    visit_count[source] -= 1

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
    visited[key] = 0

print(numPaths('start', 'end', visited, False, []))

#for path in paths:
    #print(path)
