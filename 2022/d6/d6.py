import re

with open('input.txt', 'r') as infile:
    line = infile.read().strip()

for i in range(3, len(line)):
    if len(set([line[i], line[i-1], line[i-2], line[i-3]])) == 4:
        print(i+1)
        break
