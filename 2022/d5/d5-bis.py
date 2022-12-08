import re

def command(command_str):
    match = re.match(r"move (\d+) from (\d) to (\d)", command_str)
    # [<amount>, <from_col>, <to_col>]
    return [int(match.group(1)), int(match.group(2)) - 1, int(match.group(3)) - 1]

# Now moves all of the boxes at once, preserving order
def move(amount, stack_from, stack_to):
    stack_to.extend(stack_from[len(stack_from)-amount:])
    for _ in range(amount):
        stack_from.pop()

numcols = 9
with open('input.txt', 'r') as infile:
    # Parse stack info
    inp = infile.read()

    stacks = [[] for i in range(numcols)]
    stack_lines = [line for line in inp.split('\n\n')[0].splitlines()]
    #print(lines)
    for col in range(numcols):
        for line in stack_lines[:len(stack_lines)-1]:
            line_idx = 4 * col + 1
            if line[line_idx].strip():
                stacks[col].append(line[line_idx])

    # reverse them because we were reading them from top to bottom
    for stack in stacks:
        stack.reverse()


    # Parse commands info
    commands = [command(line) for line in inp.split('\n\n')[1].splitlines()]
print(stacks)

for command in commands:
    move(command[0], stacks[command[1]], stacks[command[2]]) 
    print("after command")
    print(stacks)

# print(stacks)
for stack in stacks:
    print(stack[-1])
