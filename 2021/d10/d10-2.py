score_for_char = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

closing = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

def syntax_score(line):
    q = []
    for c in line:
        if c in ['(', '[', '{', '<']:
            q.append(c)
        else:
            if len(q) == 0 or c != closing[q[-1]]:
                return 0
            else:
                q.pop()

    score = 0
    for c in reversed(q):
        score *= 5
        score += score_for_char[closing[c]]

    return score

with open('input.txt') as infile:
    lines = [l.strip(' \n') for l in infile.readlines()]

scores = []
for line in lines:
    ss = syntax_score(line)
    if ss > 0:
        scores.append(ss)

middle_score = sorted(scores)[len(scores)/2]
print(middle_score)

