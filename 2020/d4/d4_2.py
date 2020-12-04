import re

def between(x, a, b):
    return a <= x and x <= b

def field_between(field, minVal, maxVal):
    field = int(field)
    return between(field, minVal, maxVal)

def byr_constraint(byr):
    return field_between(byr, 1920, 2002)

def iyr_constraint(iyr):
    return field_between(iyr, 2010, 2020)

def eyr_constraint(eyr):
    return field_between(eyr, 2020, 2030)

def hgt_constraint(hgt):
    pattern = r'([0-9]*)(cm|in)'
    match = re.search(pattern, hgt)
    if match == None: return False
    if match.group(2) == 'cm':
        return field_between(int(match.group(1)), 150, 193)
    elif match.group(2) == 'in':
        return field_between(int(match.group(1)), 59, 76)
    else:
        print('error at parsing the height field ' + hgt)

def hcl_constraint(hcl):
    pattern = r'#([0-9]|[a-f]){6}$'
    return bool(re.match(pattern, hcl))

def ecl_constraint(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def pid_constraint(pid):
    pattern = r'^\d{9}$'
    m = re.match(pattern, pid)
    print(m)
    return bool(re.match(pattern, pid))


def isValidPassport(rawPasspString):
    passportStr = rawPasspString.replace('\n', ' ')
    passportDetails = passportStr.split(' ')
    constraints = [
            ('byr', byr_constraint), 
            ('iyr', iyr_constraint), 
            ('eyr', eyr_constraint), 
            ('hgt', hgt_constraint), 
            ('hcl', hcl_constraint),
            ('ecl', ecl_constraint),
            ('pid', pid_constraint)
    ]
   
    passportDict = {}
    for keyValStr in passportDetails:
        keyVal = keyValStr.split(':')
        passportDict[keyVal[0]] = keyVal[1] 

    constraintsAcomplished = [(x[0] in passportDict) and x[1](passportDict[x[0]]) for x in constraints]
#    print(passportStr)
#    print(constraintsAcomplished)
    return all(constraintsAcomplished)

with open('d4_input.txt', 'r') as infile:
    lines = infile.read().rstrip('\n').split('\n\n')
#    print(len(lines))    
    print(sum(map(lambda passport: isValidPassport(passport), lines)))
