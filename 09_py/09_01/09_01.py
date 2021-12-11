def checkSourrounding(map, position):
    lowestPoints = [[False for _ in range(3)] for _ in range(3)]
    minimum = 10

    for i in range(-1,2):
        for j in range(-1,2):
            x = position[0]+i
            y = position[1]+j
            if abs(i) == 1 and abs(j) == 1:
                continue
            elif 0 <= y < len(map):
                if 0 <= x < len(map[0]):
                    minimum = min(minimum, map[y][x])

    for i in range(-1,2):
        for j in range(-1,2):
            x = position[0]+i
            y = position[1]+j
            if abs(i) == 1 and abs(j) == 1:
                continue
            elif 0 <= y < len(map):
                if 0 <= x < len(map[0]):
                    if map[y][x] == minimum:
                        lowestPoints[i+1][j+1] = True

    if(sum(sum(lowestPoints, [])) > 1):
        lowestPoints[1][1] = False

    return lowestPoints


with open('input.txt') as f:
    lines = f.readlines()

mapHeight = []
for line in lines:
    mapHeight.append(list(map(int, list(line.strip()))))


totalSum = 0
lowCounter = 0
for i in range(len(mapHeight[0])):
    for j in range(len(mapHeight)):
        lowestPoint = checkSourrounding(mapHeight, (i,j))
        if lowestPoint[1][1] == True:
            lowPoint = mapHeight[j][i]
            totalSum += lowPoint + 1
            lowCounter += 1

print("Sum: ")
print(totalSum)
print("Counter: ")
print(lowCounter)

