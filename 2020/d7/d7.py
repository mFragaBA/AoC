import re

FOUND = 1
rules = {}
count = 0

def make_rule(ruleStr):
    pattern = r'(.*)\sbags\scontain\s(.*)'
    match = re.search(pattern, ruleStr)

    outerBag = match.group(1).replace(" ", "_")
    valStr = match.group(2)
    innerBags = valStr.strip()
    bagList = []
    if innerBags != 'no other bags':
        innerBags = innerBags.split(',')
        for bagRule in innerBags:
            bagPattern = r'(\d+)\s(.*)\sbags?'
            bagMatch = re.search(bagPattern, bagRule)
            quantity = int(bagMatch.group(1))
            bag = bagMatch.group(2)
            bag = bag.replace(" ", "_")
            bagList.append([bag, quantity])
    rule = [outerBag, bagList]
    return rule
    


def dfs_find(bag, obj, visited):
    if bag == obj:
        return True
    
    visited[bag] = 0
    if not bag in rules:
        return False
    else:
        for innerBag in rules[bag]:
            if innerBag[0] in visited:
                continue
            if dfs_find(innerBag[0], obj, visited):
                return True

    return False


with open('d7_input.txt', 'r') as infile:
    lines = infile.read().splitlines()

    for line in lines:
        rule = make_rule(line.rstrip('.'))
        rules[rule[0]] = rule[1]
        
    for item in rules:
        if item == 'shiny_gold':
            continue
        visited = {}
        if dfs_find(item, 'shiny_gold', visited):
            count = count + 1
    print(count)
