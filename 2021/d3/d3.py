def mostCommon(l):
    if l.count('0') > l.count('1'):
        return '0'
    else:
        return '1'

def leastCommon(l):
    if l.count('0') > l.count('1'):
        return '1'
    else:
        return '0'

with open('input.txt') as infile:
    contents = [l.strip(' \n') for l in infile.readlines()]

epsilon = []
gamma = []

for bit_idx in range(len(contents[0])):
    gamma.append(mostCommon([x[bit_idx] for x in contents]))
    epsilon.append(leastCommon([x[bit_idx] for x in contents]))

epsilon = ''.join(epsilon)
gamma = ''.join(gamma)

epsilon = int(epsilon, 2)
gamma = int(gamma, 2)

print(epsilon*gamma)
