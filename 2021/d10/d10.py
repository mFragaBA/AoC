score_for_char = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
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
                #print("expected {}, but found {} instead".format(q[-1], c))
                return score_for_char[c]
            else:
                q.pop()

    return 0

with open('input.txt') as infile:
    lines = [l.strip(' \n') for l in infile.readlines()]

score = 0
for line in lines:
    ss = syntax_score(line)
    print("syntax_score: " + str(ss))
    score += ss
print(score)
