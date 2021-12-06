def simulateDay(population):
    newDayPopulation = [0 for _ in range(9)]
    for j in range(1, 9):
        newDayPopulation[j-1] = population[j]
    newDayPopulation[6] += population[0]
    newDayPopulation[8] = population[0]

    return newDayPopulation


with open('input.txt') as infile:
    lines = [l.strip(' \n') for l in infile.readlines()]

inp = [int(x) for x in lines[0].split(',')]
population = [0 for _ in range(9)]

for ind in inp:
    population[ind] += 1

for d in range(256):
    population = simulateDay(population)

print(sum(x for x in population))
