with open('input.txt', 'r') as infile:
    lines = [line.split() for line in infile.read().splitlines()]

scores = {
    "X": 1,
    "Y": 2,
    "Z": 3
} 

def result_score(theirs, mine):
    match (theirs, mine):
        case ("A", "X"): return 3
        case ("B", "Y"): return 3
        case ("C", "Z"): return 3
        case ("A", "Y"): return 6
        case ("A", "Z"): return 0
        case ("B", "X"): return 0
        case ("B", "Z"): return 6
        case ("C", "X"): return 6
        case ("C", "Y"): return 0


total_score = 0
for round in lines:
    theirs = round[0]
    mine = round[1]
    total_score += scores[mine]
    total_score += result_score(theirs, mine)

print(total_score)
