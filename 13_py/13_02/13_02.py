import re


def folding(dotMap, foldAxis, foldCoord, maxX, maxY):
    if foldAxis == 'y':
        newMaxY = foldCoord
        newMaxX = maxX
    else:
        newMaxY = maxY
        newMaxX = foldCoord

    newDotMap = [[False for _ in range(newMaxX)] for _ in range(newMaxY)]

    for xCnt in range(newMaxX):
        for yCnt in range(newMaxY):
            newDotMap[yCnt][xCnt] = dotMap[yCnt][xCnt]

    if foldAxis == 'y':
        for xCntFold in range(maxX):
            for yCntFold in range(foldCoord+1, maxY):
                if dotMap[yCntFold][xCntFold]:
                    newDotMap[foldCoord-(yCntFold-foldCoord)][xCntFold] = dotMap[yCntFold][xCntFold]

    else:
        for xCntFold in range(foldCoord+1, maxX):
            for yCntFold in range(maxY):
                if dotMap[yCntFold][xCntFold]:
                    newDotMap[yCntFold][foldCoord-(xCntFold-foldCoord)] = dotMap[yCntFold][xCntFold]

    return newDotMap, newMaxX, newMaxY


with open('input.txt') as f:
    lines = f.readlines()

coordinates = []
foldInstructions = []

for line in lines:
    print(line)

    if line.find(",") >= 0:
        match = re.search("(.*),(.*)", line)
        xVal = int(match.group(1))
        yVal = int(match.group(2))
        coordinates.append((xVal, yVal))

    elif line != "\n":
        match = re.search(".*(\w)=(.*)", line)
        foldAxis = match.group(1)
        foldCoord = int(match.group(2))
        foldInstructions.append((foldAxis, foldCoord))

maxX = 0
maxY = 0
for x, y in coordinates:
    maxX = max(x+1, maxX)
    maxY = max(y+1, maxY)

dotMap = [[False for _ in range(maxX)] for _ in range(maxY)]

for x, y in coordinates:
    dotMap[y][x] = True

dotMap, maxX, maxY = folding(dotMap, foldInstructions[0][0], foldInstructions[0][1], maxX, maxY)

result = 0
for row in dotMap:
    result += sum(row)


print(result)
print("Done")