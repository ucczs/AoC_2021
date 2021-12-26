def checkForFreeSpace(cMap, pos, east):
    freeSpace = False
    if east:
        maxXPos = len(cMap[0])
        nextXPos = pos[0]+1 
        if nextXPos >= maxXPos:
            nextXPos = 0

        if cMap[pos[1]][nextXPos] == ".":
            freeSpace = True
    else:
        maxYPos = len(cMap)
        nexYXPos = pos[1]+1 
        if nexYXPos >= maxYPos:
            nextYPos = 0

        if cMap[nextYPos][pos[0]] == ".":
            freeSpace = True

    return freeSpace


def performEastStep(cMap):
    movedAtAll = False
    newMap = []
    newRow = []
    cMoved = False

    for y, row in enumerate(cMap):
        newRow = []
        for x, symbol in enumerate(row):
            if cMoved:
                newRow.append(">")
                cMoved = False
            elif symbol != ">":
                newRow.append(symbol)
            elif checkForFreeSpace(cMap, (x, y), True):
                movedAtAll = True
                cMoved = True
                newRow.append(".")
            else:
                newRow.append(symbol)

        if cMoved:
            newRow[0] = ">"
            cMoved = False

        newMap.append(newRow)

    return newMap, movedAtAll


def rotateUp(cMap):
    rotMap = [["." for _ in range(len(cMap))] for _ in range(len(cMap[0]))]
    maxX = len(cMap[0]) - 1
    for y, row in enumerate(cMap):
        for x, symbol in enumerate(row):
            rotXPos = y
            rotYPos = maxX - x
            rotMap[rotYPos][rotXPos] = ">" if symbol == "v" else "^" if symbol == ">" else symbol

    return rotMap


def rotateDown(cMap):
    rotMap = [["." for _ in range(len(cMap))] for _ in range(len(cMap[0]))]
    maxY = len(cMap) - 1
    for y, row in enumerate(cMap):
        for x, symbol in enumerate(row):
            rotXPos = maxY - y
            rotYPos = x
            rotMap[rotYPos][rotXPos] = ">" if symbol == "^" else "v" if symbol == ">" else symbol

    return rotMap


def performSouthStep(cMap):
    rotMap = rotateUp(cMap)
    newMap, movedAtAll = performEastStep(rotMap)
    rotMap = rotateDown(newMap)

    return rotMap, movedAtAll


def printMap(cMap):
    print("Printing map:")
    for row in cMap:
        print("".join(row))


with open('input.txt') as f:
    lines = f.readlines()

cMap = []
for line in lines:
    cMap.append(list(line.strip()))

eastStepDone = True
southStepDone = True

printMap(cMap)


stepCnt = 0
while(eastStepDone or southStepDone):
    cMap, eastStepDone = performEastStep(cMap)
    cMap, southStepDone = performSouthStep(cMap)
    stepCnt += 1

print(stepCnt)