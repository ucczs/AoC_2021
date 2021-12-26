import re
import math
import itertools


def isTargetHit(xVelo, yVelo, XMinTarget, XMaxTarget, YMinTarget, YMaxTarget):
    notOvershoot = True
    currXPos = 0
    currYPos = 0
    TargetHit = False

    while(notOvershoot and not TargetHit):
        currXPos += xVelo
        currYPos += yVelo

        if currXPos >= XMinTarget and currXPos <= XMaxTarget:
            if currYPos >= YMinTarget and currYPos <= YMaxTarget:
                TargetHit = True

        if currXPos > XMaxTarget or currYPos < YMinTarget:
            notOvershoot = False

        xVelo = max(0, xVelo-1)
        yVelo -= 1

    return TargetHit


with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line)
    match = re.search("target area: x=(.*)\.\.(.*), y=(.*)\.\.(.*)", line)

xMinTarget = int(match.group(1))
xMaxTarget = int(match.group(2))
yMinTarget = int(match.group(3))
yMaxTarget = int(match.group(4))

possibleXPos = [i for i in range(xMaxTarget+2)]
possibleYPos = [i for i in range(yMinTarget-2, 140)]

positions = []

for pos in itertools.product(possibleXPos, possibleYPos):
    if isTargetHit(pos[0], pos[1], xMinTarget, xMaxTarget, yMinTarget, yMaxTarget):
        positions.append(pos)

print(len(positions))