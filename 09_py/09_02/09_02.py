from itertools import combinations_with_replacement

def checkSourrounding(map, position):
    lowestPoints = [[False for _ in range(3)] for _ in range(3)]
    minimum = 10

    for combi in combinations_with_replacement([-1,0,1], 2):
        x = position[0] + combi[0]
        y = position[1] + combi[1]
        if abs(combi[0]) == 1 and abs(combi[1]) == 1:
            continue
        elif 0 <= y < len(map):
            if 0 <= x < len(map[0]):
                minimum = min(minimum, map[y][x])

    for combi in combinations_with_replacement([-1,0,1], 2):
        x = position[0] + combi[0]
        y = position[1] + combi[1]
        if abs(combi[0]) == 1 and abs(combi[1]) == 1:
            continue
        elif 0 <= y < len(map):
            if 0 <= x < len(map[0]):
                if map[y][x] == minimum:
                    lowestPoints[combi[0]+1][combi[1]+1] = True

    if(sum(sum(lowestPoints, [])) > 1):
        lowestPoints[1][1] = False

    return lowestPoints


def checkIfSourroundingBasin(map, position, basin):
    value = map[position[1]][position[0]]
    basinVal = basin[position[1]][position[0]]

    for i in range(-1,2):
        for j in range(-1,2):
            x = position[0]+i
            y = position[1]+j

            if abs(i) == 1 and abs(j) == 1:
                continue
            elif 0 <= y < len(map):
                if 0 <= x < len(map[0]):
                    if map[y][x] > value and map[y][x] < 9:
                        basin[y][x] = basinVal


def findThreeLargest(basinMap, basinCount):
    threeLargest = [0, 0, 0]
    for i in range(1, basinCount+1):
        numbCount = 0
        for row in basinMap:
            numbCount += row.count(i)
        
        for largest in threeLargest:
            if numbCount > largest:
                threeLargest[0] = numbCount
                threeLargest = sorted(threeLargest)
                break

    return threeLargest


with open('input.txt') as f:
    lines = f.readlines()

mapHeight = []
for line in lines:
    mapHeight.append(list(map(int, list(line.strip()))))

basinMap = [[0 for _ in range(len(mapHeight[0]))] for _ in range(len(mapHeight))]

counter = 0
for i in range(len(mapHeight[0])):
    for j in range(len(mapHeight)):
        lowestPoint = checkSourrounding(mapHeight, (i,j))
        if lowestPoint[1][1] == True:
            counter += 1
            basinMap[j][i] = counter

for _ in range(10):
    for i in range(len(mapHeight[0])):
        for j in range(len(mapHeight)):
            if basinMap[j][i] > 0:
                checkIfSourroundingBasin(mapHeight, (i,j), basinMap)

basinCount = 0
for row in basinMap:
    basinCount = max(max(row), basinCount)

threeLargest = findThreeLargest(basinMap, basinCount)

sum = 1
for largest in threeLargest:
    sum *= largest

missing = 0
for i in range(len(mapHeight[0])):
    for j in range(len(mapHeight)):
        if basinMap[j][i] == 0 and mapHeight[j][i] != 9:
            missing += 1

print(missing)
print(sum)
print("Done")
