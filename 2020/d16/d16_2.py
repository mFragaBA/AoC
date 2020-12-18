def makeRule(ruleStr):
    spltRule = ruleStr.split(':')
    key = spltRule[0]
    intervals = [(int(r.strip().split('-')[0]), int(r.strip().split('-')[1])) for r in spltRule[1].split('or')]

    return (key, intervals)

def isInvalidValue(num, ranges):
    return all(not any(r[0] <= num <= r[1] for r in rangeList) for rangeList in ranges)

def isValidTicket(ticket, intervals):
    return all(not isInvalidValue(value, intervals) for value in ticket)

def isValidOrderForRule(rule, rulesD, tickets, order):
    return all(any(r[0] <= ticket[order] <= r[1] for r in rulesD[rule]) for ticket in tickets)

#finds order for the rules assigning orders
def findOrder(tickets, rules, rulesD, orderMask, rulesCandidates, orders, i):
    if i == len(rules):
        return True
    
    rule = rules[i]

    for order in rulesCandidates[rule]:
        if orderMask[order] == -1 and isValidOrderForRule(rule, rulesD, tickets, order):
            orderMask[order] = 0
            if findOrder(tickets, rules, rulesD, orderMask, rulesCandidates, orders, i+1):
                orders.append((rule, order))
                return True
            orderMask[order] = -1

    return False

def candidates(rulesD, rule, tickets):
    return [i for i in range(len(rulesD)) if isValidOrderForRule(rule, rulesD, tickets, i)]

with open('d16_input.txt', 'r') as infile:
    lines = infile.read().split('\n\n')
    rules = [makeRule(r) for r in lines[0].splitlines()]
    rulesD = {}

    for rule in rules:
        rulesD[rule[0]] = rule[1]

    ranges = rulesD.values()

    myTicket = [int(value) for value in lines[1].splitlines()[1].split(',')]
    otherTickets = [[int(value) for value in ticket.split(',')] for ticket in lines[2].splitlines()[1:]]
    otherTickets = [myTicket] + [ticket for ticket in otherTickets if isValidTicket(ticket, ranges)]

    print('ticket amount is', len(otherTickets))

    orderMask = [-1 for _ in range(len(rules))]
    rulesCandidates = {}
    for rule in rulesD:
        rulesCandidates[rule] = candidates(rulesD, rule, otherTickets) 

    print(rulesCandidates)

    fixedRules = [r for r in rulesCandidates if len(rulesCandidates[r]) == 1]
    orders = []
    while len(fixedRules) > 0:
        for r in fixedRules:
            orderMask[rulesCandidates[r][0]] = 0
            orders.append((r, rulesCandidates[r][0]))
        
        for r in rulesCandidates:
            rulesCandidates[r] = [candidate for candidate in rulesCandidates[r] if orderMask[candidate] == -1]

        fixedRules = [r for r in rulesCandidates if len(rulesCandidates[r]) == 1]

    print(orders)

    findOrder(otherTickets, list(rulesD.keys()), rulesD, orderMask, rulesCandidates, orders, 0)

    print(orders)


    mult = 1
    for ruleOrder in orders:
        if ruleOrder[0].startswith('departure'):
            mult = mult * myTicket[ruleOrder[1]]

    print(mult)

