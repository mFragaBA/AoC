def updateWithNum(num, turns, turn):
    if num in turns:
        if len(turns[num]) == 1:
            turns[num].append(turn)
        else:
            turns[num][0] = turns[num][1]
            turns[num][1] = turn
    else:
        turns[num] = [turn]


turns = {
        11: [1],
        18: [2], 
        0: [3], 
        20: [4],
        1: [5],
        7: [6],
        16: [7]
}
lastNum = 16
turn = 8
for _ in range(30000000 - 7):
    if len(turns[lastNum]) == 1:
        lastNum = 0
        updateWithNum(0, turns, turn)
    else:
        diff = turns[lastNum][1] - turns[lastNum][0]
        lastNum = diff
        updateWithNum(diff, turns, turn)

    #print("turno", turn, lastNum)
    turn += 1
print("turno", turn-1, lastNum)

        
