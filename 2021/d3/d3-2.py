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

oxygenRating = [s for s in contents]
CO2Rating = [s for s in contents]

for bit_idx in range(len(contents[0])):
    mc = mostCommon([x[bit_idx] for x in oxygenRating])
    lc = leastCommon([x[bit_idx] for x in CO2Rating])

    if len(oxygenRating) > 1:
        oxygenRating = [x for x in oxygenRating if x[bit_idx] == mc]
    if len(CO2Rating) > 1:
        CO2Rating = [x for x in CO2Rating if x[bit_idx] == lc]

    print(bit_idx)
    print(mc)
    print(lc)

    print(oxygenRating)
    print(CO2Rating)

oxygenRating = int(oxygenRating[0], 2)
CO2Rating = int(CO2Rating[0], 2)

print(oxygenRating*CO2Rating)
