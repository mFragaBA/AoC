import re

class Rule:
    
    def buildPattern(self, rulesDict):
        candidatesRules = ["".join([(("(" + rules[ruleId].buildPattern(rulesDict) + ")") if ruleId in rules else ruleId[1:-1]) for ruleId in candidate]) for candidate in self.candidates]
        self.pattern = '|'.join(["(" + candidate + ")" for candidate in candidatesRules])
        return self.pattern
    
    def getPattern(self):
        return self.pattern

    def __init__(self, ruleStr):
        self.candidates = [s.strip().split(' ') for s in ruleStr.split('|')]


with open('d19_input.txt', 'r') as infile:
    lines = infile.read()
    
    rules = {}
    for ruleStr in lines.split('\n\n')[0].splitlines():
        splitRule = ruleStr.split(':')
        ruleId = splitRule[0]
        rules[ruleId] = Rule(splitRule[1])

    for ruleId in rules:
        rules[ruleId].buildPattern(rules)

    messages = lines.split('\n\n')[1].splitlines()

    def mainMatch(s):
        expandedEleven = []
        for i in range(1, 5):
            patt = '(' + (( '(' + rules['42'].pattern + ')') * i) + (('(' + rules['31'].pattern + ')') * i) + ')'
            expandedEleven.append(patt)
        pattern = '^(' + rules['42'].pattern + ')+' + '(' + '|'.join(expandedEleven) + ')$'
        m = re.match(pattern, s)
        return bool(m)


    print(sum(int(mainMatch(s)) for s in messages))

