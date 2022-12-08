import re

with open('input.txt', 'r') as infile:
    line = infile.read().strip()

for i in range(13, len(line)):
    bytes = [line[j] for j in range(i-13, i+1)]
    
    if len(set(bytes)) == 14:
        print(i+1)
        break
