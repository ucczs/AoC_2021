
def performTrainingTurn(score, diceIdx, diceOrder, currentPos):
    rolledSum = diceOrder[diceIdx%100] + diceOrder[(diceIdx+1)%100] + diceOrder[(diceIdx+2)%100]
    currentPos = currentPos + rolledSum
    if currentPos > 10:
        currentPos -= int(currentPos/10) * 10
    score += currentPos

    return currentPos, score

p1_score = 0
p2_score = 0

with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line)
    if line.find("Player 1") >= 0:
        p1_pos = int(line.strip()[-1])
    else:
        p2_pos = int(line.strip()[-1])

diceOrder = [i for i in range(1,101)]

target = 1000
targetReached = False
p1_turn = True
diceIdx = 0
rollCnt = 0

while(not targetReached):
    rollCnt += 3
    if p1_turn:
        p1_pos, p1_score = performTrainingTurn(p1_score, diceIdx, diceOrder, p1_pos)
    else:
        p2_pos, p2_score = performTrainingTurn(p2_score, diceIdx, diceOrder, p2_pos)

    if p1_score >= 1000 or p2_score >= 1000:
        targetReached = True

    p1_turn = not p1_turn
    diceIdx = (diceIdx + 3) % 100


result = min(p1_score, p2_score) * rollCnt

print(result)
print("Done")



