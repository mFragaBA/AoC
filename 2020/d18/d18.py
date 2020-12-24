def tokenize(l):
    splittedL = l.split(' ')
    tokenized = []
    for t in splittedL:
        if t[0] == '(':
            i = 0
            while t[i] == '(':
                tokenized.append(t[i])
                i += 1
            tokenized.append(t[i:])
        elif t[-1] == ')':
            i = len(t) - 1
            while t[i] == ')':
                i -= 1
            tokenized.append(t[:i+1])
            tokenized += [')' for _ in range(len(t) - i - 1)]
        else:
            tokenized.append(t)

    return tokenized

def _calculate(sumsOrProds):
    i = 1
    aux = int(sumsOrProds[0])
    while i < len(sumsOrProds):
        if sumsOrProds[i] == '+':
            aux += int(sumsOrProds[i+1])
        elif sumsOrProds[i] == '*':
            aux *= int(sumsOrProds[i+1])
        else:
            print('something went wrong')
        i += 2

    return aux



def calculate(line):
    print(line)
    tokenizedLine = tokenize(line)
    stack = []

    for token in tokenizedLine:
        if token[-1] == ')':
            innerParent = []
            while stack[-1] != '(':
                innerParent.append(stack[-1])
                stack.pop()
            stack.pop()
            innerParent.reverse()
            stack.append(_calculate(innerParent))
                
        else:
            stack.append(token)
        print(stack)
            
    return _calculate(stack)

with open('d18_input.txt', 'r') as infile:
    lines = infile.read().splitlines()
    print(sum(calculate(l) for l in lines))
