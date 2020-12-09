

with open('d8_input.txt', 'r') as infile:
    lines = infile.read().splitlines()

    acc = 0
    lineno = 0

    executedLines = []
    while not lineno in executedLines:
        executedLines.append(lineno)
        line = lines[lineno]
        op = line[:3]
        sign = -1 if line[4] == '-' else 1
        val = int(line[5:])

        if op == 'acc':
            acc = acc + sign * val
            lineno = lineno + 1
        elif op == 'jmp':
            lineno = lineno + sign * val
        else:
            lineno = lineno + 1

    print(acc)
