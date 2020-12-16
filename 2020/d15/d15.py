def updateWithNum(num, turns, occurrences, turn):
    if num in turns:
        j = turns.index(num)
        if len(occurrences[j]) == 1:
            occurrences[j].append(turn)
        else:
            occurrences[j][0] = occurrences[j][1]
            occurrences[j][1] = turn
    else:
        turns.append(num)
        occurrences.append([turn])


turns = [11, 18, 0, 20, 1, 7, 16]
occurrences = [[t] for t in range(1,len(turns)+1)]
lastNum = turns[-1]
turn = len(turns) + 1
for _ in range(2013):
    i = turns.index(lastNum)
    if len(occurrences[i]) == 1:
        lastNum = 0
        updateWithNum(0, turns, occurrences, turn)
    else:
        diff = occurrences[i][1] - occurrences[i][0]
        lastNum = diff
        updateWithNum(diff, turns, occurrences, turn)
    
    print("turno", turn, lastNum)
    turn += 1

        
