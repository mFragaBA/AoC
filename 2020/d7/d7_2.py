import re

rules = {}

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
    
def dfs_count(bag):
    suma = 1
    if len(rules[bag]) == 0:
        return suma
    else:
        for innerBag in rules[bag]:
            suma = suma + innerBag[1] * dfs_count(innerBag[0])

    return suma


with open('d7_input.txt', 'r') as infile:
    lines = infile.read().splitlines()

    for line in lines:
        rule = make_rule(line.rstrip('.'))
        rules[rule[0]] = rule[1]
        
    print(dfs_count('shiny_gold') - 1)
