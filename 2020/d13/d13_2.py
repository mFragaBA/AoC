from functools import reduce

def chinese_remainder(n, a):
    suma = 0
    prod=reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p= prod // n_i
        suma += a_i* mul_inv(p, n_i)*p
    return suma % prod

def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b == 1: return 1
    while a>1 :
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1<0 : x1 += b0
    return x1

with open('d13_input.txt', 'r') as infile:
    lines = infile.read().splitlines()
    goal = int(lines[0])
    lines = lines[1].split(',')
    
    n = []
    a = []
    tAdd = 0
    for line in lines:
        if line != 'x':
            n.append(int(line)) 
            a.append(int(line) - tAdd)

        tAdd += 1

    print(n)
    print(a)

    print(chinese_remainder(n, a))

