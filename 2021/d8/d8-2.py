def findDigitsWires(input_values):
    numbers_by_wire_amount = {
        2: [1],
        3: [7],
        4: [4],
        5: [2, 3, 5],
        6: [0, 6, 9],
        7: [8]
    }


    mid_top = ' '
    mid_mid = ' '
    mid_bottom = ' '
    top_left = ' '
    bottom_left = ' '
    top_right = ' '
    bottom_right = ' '

    used = set()

    # Find 1
    for val in input_values:
        if len(val) == 2:
            bottom_right = val[0]
            top_right = val[1]
            used.add(bottom_right)
            used.add(top_right)

    # Find 7
    for val in input_values:
        if len(val) == 3:
            for c in val:
                if c != bottom_right and c != top_right:
                    mid_top = c
                used.add(c)

    # Find 4
    for val in input_values:
        if len(val) == 4:
            for c in val:
                used.add(c)

    # Find 3 (uses the same as 1)
    for val in input_values:
        if len(val) == 5 and top_right in val and bottom_right in val:
            for c in val:
                if c not in used:
                    mid_bottom = c
                    used.add(c)
            for c in val:
                if c != mid_bottom and c != mid_top and c != bottom_right and c != top_right:
                    mid_mid = c

    # now that i know mid mid i know top right
    for val in input_values:
        if len(val) == 4:
            for c in val:
                if c != mid_mid and c != bottom_right and c != top_right:
                    top_left = c

    # Find 0 (does not use the middle one used in 4)
    for val in input_values:
        if len(val) == 6 and mid_mid not in val:
            bottom_left = [c for c in val if c not in used][0]

    # Find 2 and fix the order of the right side if it needs to
    for val in input_values:
        if len(val) == 5 and bottom_left in val:
            for c in val:
                if c == bottom_right:
                    temp = bottom_right
                    bottom_right = top_right
                    top_right = temp
    
    mappings = [
            ("0", set([mid_top, mid_bottom, top_left, top_right, bottom_left, bottom_right])), 
            ("1", set([top_right, bottom_right])),
            ("2", set([top_right, bottom_left, mid_mid, mid_top, mid_bottom])),
            ("3", set([top_right, bottom_right, mid_mid, mid_top, mid_bottom])),
            ("4", set([top_right, bottom_right, mid_mid, top_left])),
            ("5", set([top_left, bottom_right, mid_mid, mid_top, mid_bottom])),
            ("6", set([top_left, bottom_left, bottom_right, mid_mid, mid_top, mid_bottom])),
            ("7", set([top_right, bottom_right, mid_top])),
            ("8", set([top_right, bottom_right, top_left, bottom_left, mid_mid, mid_top, mid_bottom])),
            ("9", set([top_right, bottom_right, top_left, mid_mid, mid_top, mid_bottom])),
    ]

    return mappings

def digit(ov, mappings):
    ovSet = set([c for c in ov])
    for mapping in mappings:
        if ovSet == mapping[1]:
            return mapping[0]

    print("error")
    return None

with open('input.txt') as infile:
    lines = [l.strip(' \n') for l in infile.readlines()]

input_values = [l.split('|')[0].split(' ') for l in lines]
output_values = [l.split('|')[1].split(' ') for l in lines]

full_sum = 0
for i in range(len(lines)):
    input_values[i].pop()
    digits = findDigitsWires(input_values[i])
    
    number = int(''.join([digit(o, digits) for o in output_values[i] if o != '']))

    full_sum += number
    

print(full_sum)
