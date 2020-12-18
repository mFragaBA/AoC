def makeRule(ruleStr):
    spltRule = ruleStr.split(':')
    key = spltRule[0]
    intervals = [(int(r.strip().split('-')[0]), int(r.strip().split('-')[1])) for r in spltRule[1].split('or')]

    return (key, intervals)

def isInvalid(num, ranges):
    return all(not any(r[0] <= num <= r[1] for r in rangeList) for rangeList in ranges)

with open('d16_input.txt', 'r') as infile:
    lines = infile.read().split('\n\n')
    rules = [makeRule(r) for r in lines[0].splitlines()]
    rulesD = {}

    for rule in rules:
        rulesD[rule[0]] = rule[1]

    ranges = rulesD.values()

    #myTicket = lines[1].splitlines()[1]
    otherTickets = [[int(value) for value in ticket.split(',')] for ticket in lines[2].splitlines()[1:]]

    errorRate = sum(sum(value for value in ticket if isInvalid(value, ranges)) for ticket in otherTickets)

    print(errorRate)
