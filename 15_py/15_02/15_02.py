import sys
import copy

def createMap(originalMap):
    factor = 5
    newMap = [[0 for _ in range(len(originalMap[0])*factor)] for _ in range(len(originalMap)*factor)]
    for xi in range(factor):
        for yi in range(factor):
            for x in range(len(originalMap[0])):
                for y in range(len(originalMap)):
                    xNewMap = xi * len(originalMap[0]) + x
                    yNewMap = yi * len(originalMap) + y
                    newValue = originalMap[y][x]+xi+yi
                    newValue = newValue-9 if originalMap[y][x]+xi+yi > 9 else newValue
                    newMap[yNewMap][xNewMap] = newValue

    return newMap


def getValuesAroundCoordinate(mapValues, x, y):
    try:
        valueUp = mapValues[y+1][x]
    except IndexError:
        valueUp = -1

    try:
        valueDown = mapValues[y-1][x]
    except IndexError:
        valueDown = -1

    try:
        valueLeft = mapValues[y][x-1]
    except IndexError:
        valueLeft = -1

    try:
        valueRight = mapValues[y][x+1]
    except IndexError:
        valueRight = -1

    return (valueUp, valueRight, valueDown, valueLeft)


def initializeSumMap(riskMap):
    sumMap = [[0 for _ in range(len(riskMap[0]))] for _ in range(len(riskMap))]

    for x in range(len(riskMap[0])):
        for y in range(len(riskMap)):
            if x == 0 and y == 0:
                pass
            else:
                if x == 0:
                    sumMap[y][x] = sumMap[y-1][x] + riskMap[y][x]
                elif y == 0:
                    sumMap[y][x] = sumMap[y][x-1] + riskMap[y][x]
                else:
                    sumMap[y][x] = min(sumMap[y-1][x] + riskMap[y][x], sumMap[y][x-1] + riskMap[y][x])
    return sumMap



with open('input.txt') as f:
    lines = f.readlines()

riskMap = []

for line in lines:
    print(line)
    risk = list(map(int, list(line.strip())))
    riskMap.append(risk)

riskMap = createMap(riskMap)

sumMap = initializeSumMap(riskMap)

changeInMap = True
while(changeInMap):
    sumMapBefore = copy.deepcopy(sumMap)
    for x in range(len(riskMap[0])):
        for y in range(len(riskMap)):
            if x == 0 and y == 0:
                pass
            else:
                values = getValuesAroundCoordinate(sumMap, x, y)
                minVal = sys.maxsize
                for val in values:
                    if val >= 0 and val < minVal:
                        minVal = val
                sumMap[y][x] = minVal + riskMap[y][x]

    changeInMap = not (sumMapBefore == sumMap)
    print(sumMap[-1][-1])

print(sumMap[-1][-1])