

with open('d13_input.txt', 'r') as infile:
    lines = infile.read().splitlines()
    goal = int(lines[0])
    lines = lines[1].split(',')
    
    times = []
    for line in lines:
        if line != 'x':
            times.append(int(line))


    minRemainder = times[0] * ((goal + times[0] - 1) // times[0]) - goal
    minBusID = times[0]
    for t in times:
        if (t * ((goal + t - 1) // t) - goal) < minRemainder:
            minRemainder = t * ((goal + t - 1) // t) - goal
            minBusID = t
        
    print(minBusID * minRemainder)



