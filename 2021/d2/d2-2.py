with open('input.txt') as infile:
    instructions = [i.strip(' \n').split(' ') for i in infile.readlines()]

posX = 0
posY = 0
aim = 0

for instruction in instructions:
    if instruction[0] == 'forward':
        posX += int(instruction[1])
        posY += int(instruction[1]) * aim
    elif instruction[0] == 'down':
        aim += int(instruction[1])
    elif instruction[0] == 'up':
        aim -= int(instruction[1])

print(posX * posY)


