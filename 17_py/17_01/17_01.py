import re
import math

def quadraticFormular(a, b, c):
    d = (b**2) - (4*a*c)

    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)

    return sol1, sol2


with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line)
    match = re.search("target area: x=(.*)\.\.(.*), y=(.*)\.\.(.*)", line)

XMinTarget = int(match.group(1))
XMaxTarget = int(match.group(2))
YMinTarget = int(match.group(3))
YMaxTarget = int(match.group(4))

sol1, sol2 = quadraticFormular(1,1, -XMinTarget*2)
xVelo = math.ceil(max(sol1, sol2))

yVeloValid = 0
for yVelo in range(10000):
    yMax = yVelo * (yVelo + 1) / 2
    yDiffMin = yMax + abs(YMaxTarget)
    yDiffMax = yMax + abs(YMinTarget)

    sol1Min, sol2Min = quadraticFormular(1,1, -yDiffMin*2)
    minYVelo = int(max(sol1Min, sol2Min))
    sol1Max, sol2Max = quadraticFormular(1,1, -yDiffMax*2)
    maxYVelo = int(max(sol1Max, sol2Max))

    if minYVelo != maxYVelo:
        yVeloValid = yVelo

print((xVelo, yVeloValid))

result = int(yVeloValid * (yVeloValid + 1) / 2)

print(result)
