import re


def ignoreLine(line):
    return not (line[0][0] == line[1][0] or line[0][1] == line[1][1])

def fillOutCoordinates(linesCoord, fillArray):
    for lineCoord in linesCoord:
        horizontalLine = lineCoord[0][1] == lineCoord[1][1]

        if horizontalLine:
            xDiff = lineCoord[1][0] - lineCoord[0][0]
            signMultiplier = 1
            if xDiff < 0:
                signMultiplier = -1
            for x in range(xDiff * signMultiplier + 1):
                xFill = lineCoord[0][0] + (x * signMultiplier)
                yFill = lineCoord[0][1]
                fillArray[yFill][xFill] += 1
        else:
            yDiff = lineCoord[1][1] - lineCoord[0][1]
            signMultiplier = 1
            if yDiff < 0:
                signMultiplier = -1
            for y in range(yDiff * signMultiplier + 1):
                xFill = lineCoord[0][0]
                yFill = lineCoord[0][1] + (y * signMultiplier)
                fillArray[yFill][xFill] += 1


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

    lineCoord = [(x1, y1), (x2, y2)]
    if not ignoreLine(lineCoord):
        linesCoord.append(lineCoord)

fillArray = [[0 for _ in range(xMax)] for _ in range(yMax)]
fillOutCoordinates(linesCoord, fillArray)

result = sum(sum(1 for i in row if i > 1) for row in fillArray)
print(result)
