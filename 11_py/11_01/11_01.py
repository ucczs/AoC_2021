
from itertools import combinations_with_replacement

def flashPosition(octMap, position, flashMap):
    newFlashPending = False
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                pass
            else:
                x = position[0] + i
                y = position[1] + j
                if 0 <= y < len(octMap):
                    if 0 <= x < len(octMap[0]):
                        if octMap[x][y] > 9 or flashMap[x][y] > 0:
                            pass
                        else:
                            octMap[x][y] += 1
                            if octMap[x][y] > 9:
                                newFlashPending = True

    return newFlashPending


def printMap(octMap):
    for line in octMap:
            print(line)

with open('input.txt') as f:
    lines = f.readlines()

octMap = []

for line in lines:
    print(line)
    octMap.append(list(map(int, list(line.strip()))))


flashCount = 100

printMap(octMap)
result = 0

for stepCnt in range(1, flashCount+1):
    newFlashPending = True
    flashedMap = [[0 for _ in range(len(octMap[0]))] for _ in range(len(octMap))]

    for i in range(len(octMap[0])):
        for j in range(len(octMap)):
            octMap[i][j] += 1

    while(newFlashPending):
        newFlashPending = False
        for i in range(len(octMap[0])):
            for j in range(len(octMap)):
                if octMap[i][j] > 9:
                    result += 1
                    newFlashPending = flashPosition(octMap, (i,j), flashedMap) or newFlashPending
                    flashedMap[i][j] += 1

        for i in range(len(octMap[0])):
            for j in range(len(octMap)):
                if octMap[i][j] > 9 and flashedMap[i][j] > 0:
                    octMap[i][j] = 0

    if (stepCnt % 10) == 0:
        print("--------")
        print(stepCnt)
        printMap(octMap)

