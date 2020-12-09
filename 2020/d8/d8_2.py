def simulate_code(code):
    acc = 0
    lineno = 0

    executedLines = []
    while (not lineno in executedLines) and (lineno < len(code)):
        executedLines.append(lineno)
        line = code[lineno]
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
    
    return (acc, lineno)


with open('d8_input.txt', 'r') as infile:
    lines = infile.read().splitlines()

    for lineno in range(len(lines)):
        newCode = [l for l in lines]
        if lines[lineno][:3] == 'jmp':
            newCode[lineno] = newCode[lineno].replace('jmp', 'nop')
        elif lines[lineno][:3] == 'nop':
            newCode[lineno] = newCode[lineno].replace('nop', 'jmp')

        simulationResult = simulate_code(newCode)
        if simulationResult[1] >= len(newCode):
            print(simulationResult[0])
