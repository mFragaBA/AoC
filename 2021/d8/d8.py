def countInteresingDigits(output):
    res = 0
    for num in output:
        if len(num) in [2, 3, 4, 7]:
            res += 1

    return res

with open('input.txt') as infile:
    lines = [l.strip(' \n') for l in infile.readlines()]

output_values = [l.split('|')[1].split(' ') for l in lines]

interesting_digits = 0
for output in output_values:
    interesting_digits += countInteresingDigits(output)

print(interesting_digits)
