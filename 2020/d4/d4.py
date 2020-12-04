def isValidPassport(rawPasspString):
    passportStr = rawPasspString.replace('\n', ' ')
    passportDetails = passportStr.split(' ')
    neededKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    
    for keyValStr in passportDetails:
        keyVal = keyValStr.split(':')
        if keyVal[0] in neededKeys:
            neededKeys.remove(keyVal[0])
    
    return len(neededKeys) == 0

with open('d4_input.txt', 'r') as infile:
    lines = infile.read().split('\n\n')
    
    print(sum(map(lambda passport: isValidPassport(passport), lines)))
