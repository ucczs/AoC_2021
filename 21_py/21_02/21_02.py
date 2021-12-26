savedSetups = {}
diceOrder = [1, 2, 3]

def simulateMoves(p1_pos, p2_pos, p1_score, p2_score):
    if p1_score >= 21:
        return (1,0)
    if p2_score >= 21:
        return (0,1)
    if (p1_pos, p2_pos, p1_score, p2_score) in savedSetups:
        return savedSetups[(p1_pos, p2_pos, p1_score, p2_score)]
    result = (0,0)
    for dice1 in diceOrder:
        for dice2 in diceOrder:
            for dice3 in diceOrder:
                p1_pos_new = (p1_pos+dice1+dice2+dice3)%10
                p1_score_new = p1_score + p1_pos_new + 1

                x1, y1 = simulateMoves(p2_pos, p1_pos_new, p2_score, p1_score_new)
                result = (result[0]+y1, result[1]+x1)

    savedSetups[(p1_pos, p2_pos, p1_score, p2_score)] = result
    return result



with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line)
    if line.find("Player 1") >= 0:
        p1_pos = int(line.strip()[-1])-1
    else:
        p2_pos = int(line.strip()[-1])-1

result = simulateMoves(p1_pos, p2_pos, 0, 0)

print(max(result))
print("Done")
