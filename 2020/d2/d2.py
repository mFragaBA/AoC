import re

def between(x, a, b):
    return a <= x and x <= b

def parsePasswd(passwdStr):
    pattern = r'([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)'
    m = re.search(pattern, passwdStr)
    return m.groups()

def validPasswd(passwd):
    minCount = int(passwd[0])
    maxCount = int(passwd[1])
    character = passwd[2]
    ocurrCount = passwd[3].count(character)
    return between(ocurrCount, minCount, maxCount)

with open('d2_input.txt', 'r') as infile:
    lines = infile.read().splitlines()

    passwords = [parsePasswd(line) for line in lines]

    print(sum(validPasswd(passwd) for passwd in passwords))


