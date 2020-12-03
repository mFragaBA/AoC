import re

def parsePasswd(passwdStr):
    pattern = r'([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)'
    m = re.search(pattern, passwdStr)
    return m.groups()

def validPasswd(passwd):
    firstCharIdx = int(passwd[0]) - 1
    secondCharIdx = int(passwd[1]) - 1
    character = passwd[2]
    ocurrCount = (passwd[3][firstCharIdx] == character) + (passwd[3][secondCharIdx] == character)
    return ocurrCount == 1 

with open('d2_input.txt', 'r') as infile:
    lines = infile.read().splitlines()

    passwords = [parsePasswd(line) for line in lines]

    print(sum(validPasswd(passwd) for passwd in passwords))


