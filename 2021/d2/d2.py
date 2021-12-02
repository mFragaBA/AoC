with open('input.txt') as infile:
    instructions = [i.strip(' \n').split(' ') for i in infile.readlines()]

posX = 0
posY = 0

for instruction in instructions:
    if instruction[0] == 'forward':
        posX += int(instruction[1])
    elif instruction[0] == 'down':
        posY += int(instruction[1])
    elif instruction[0] == 'up':
        posY -= int(instruction[1])

print(posX * posY)


