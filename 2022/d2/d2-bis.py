with open('input.txt', 'r') as infile:
    lines = [line.split() for line in infile.read().splitlines()]

scores = {
    "A": 1,
    "B": 2,
    "C": 3
} 

def result_score(theirs, mine):
    match (theirs, mine):
        case ("A", "X"): return 0 + scores["C"]
        case ("B", "X"): return 0 + scores["A"]
        case ("C", "X"): return 0 + scores["B"]
        case ("A", "Y"): return 3 + scores["A"]
        case ("B", "Y"): return 3 + scores["B"]
        case ("C", "Y"): return 3 + scores["C"]
        case ("A", "Z"): return 6 + scores["B"]
        case ("B", "Z"): return 6 + scores["C"]
        case ("C", "Z"): return 6 + scores["A"]


total_score = 0
for round in lines:
    theirs = round[0]
    mine = round[1]
    total_score += result_score(theirs, mine)

print(total_score)
