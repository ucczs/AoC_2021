import re


def fillOutCoordinates(linesCoord, fillArray):
    for lineCoord in linesCoord:
        xDiff = lineCoord[1][0] - lineCoord[0][0]
        yDiff = lineCoord[1][1] - lineCoord[0][1]

        signMultiplierX = 1 if xDiff > 0 else -1 if xDiff < 0 else 0 
        signMultiplierY = 1 if yDiff > 0 else -1 if yDiff < 0 else 0 

        target = lineCoord[0]
        while(target != lineCoord[1]):
            fillArray[target[1]][target[0]] += 1
            target = (target[0] + signMultiplierX,target[1] + signMultiplierY)
        fillArray[target[1]][target[0]] += 1


with open('input.txt') as f:
    lines = f.readlines()

linesCoord = []
xMax = 0
yMax = 0

for line in lines:
    print(line)
    regex = "(\d*),(\d*) -> (\d*),(\d*)"
    regexSearch = re.search(regex, line)
    x1 = int(regexSearch.group(1))
    y1 = int(regexSearch.group(2))
    x2 = int(regexSearch.group(3))
    y2 = int(regexSearch.group(4))

    xMax = max(xMax, x1+1, x2+1)
    yMax = max(yMax, y1+1, y2+1)

    linesCoord.append([(x1, y1), (x2, y2)])

fillArray = [[0 for _ in range(xMax)] for _ in range(yMax)]
fillOutCoordinates(linesCoord, fillArray)

result = sum(sum(1 for i in row if i > 1) for row in fillArray)
print(result)

