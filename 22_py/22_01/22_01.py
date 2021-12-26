import re
import sys


def doCoorinatesInOneDimensionOverlap(min1, max1, min2, max2):
    overlap = False
    if ((min1 > min2 and max1 < max2) or
        (min1 > min2 and min1 < max2 < max1) or
        (min1 < min2 < max1 and max2 > max1) or
        (min1 < min2 < max1 and min1 < max2 < max1)):
        overlap = True
    return overlap


def doTwoInstructionOverlap(instruction1, instruction2):
    overlap = False
    xMin1, xMax1 = instruction1[0][0], instruction1[0][1]
    yMin1, yMax1 = instruction1[1][0], instruction1[1][1]
    zMin1, zMax1 = instruction1[2][0], instruction1[2][1]

    xMin2, xMax2 = instruction2[0][0], instruction2[0][1]
    yMin2, yMax2 = instruction2[1][0], instruction2[1][1]
    zMin2, zMax2 = instruction2[2][0], instruction2[2][1]

    if (doCoorinatesInOneDimensionOverlap(xMin1, xMax1, xMin2, xMax2) and
        doCoorinatesInOneDimensionOverlap(yMin1, yMax1, yMin2, yMax2) and
        doCoorinatesInOneDimensionOverlap(zMin1, zMax1, zMin2, zMax2)):
        overlap = True

    return overlap


def adaptOneDimensionOnOn(minOn1, maxOn1, minOn2, maxOn2):
    adaptedDim = None
    if (minOn1 >= minOn2 and maxOn1 <= maxOn2):
        adaptedDim = [(minOn2, maxOn2)]
    elif (minOn1 >= minOn2 and minOn1 <= maxOn2 <= maxOn1):
        adaptedDim = [(minOn2, maxOn1)]
    elif (minOn1 <= minOn2 <= maxOn1 and maxOn2 >= maxOn1):
        adaptedDim = [(minOn1, maxOn2)]
    elif (minOn1 <= maxOn2 <= maxOn1 and minOn1 <= maxOn2 <= maxOn1):
        adaptedDim = [(minOn1, maxOn1)]
    else:
        print("Error, no overlaping!")
        sys.exit()

    return adaptedDim


def adaptOneDimensionOnOff(minOn, maxOn, minOff, maxOff):
    adaptedDim = None
    if (minOn >= minOff and maxOn <= maxOff):
        adaptedDim = []
    elif (minOn >= minOff and minOn <= maxOff <= maxOn):
        adaptedDim = [(maxOff+1, maxOn)]
    elif (minOn <= minOff <= maxOn and maxOff >= maxOn):
        adaptedDim = [(minOn, minOff-1)]
    elif (minOn <= maxOff <= maxOn and minOn <= maxOff <= maxOn):
        adaptedDim = [(minOn, minOff-1), (maxOff+1, maxOn)]
    else:
        print("Error, no overlaping!")
        sys.exit()

    return adaptedDim


def adaptOnOffInstruction(onInstr, offInstr):
    allNewSets = []
    newXDim = adaptOneDimensionOnOff(onInstr[0][0], onInstr[0][1], offInstr[0][0], offInstr[0][1])
    newYDim = adaptOneDimensionOnOff(onInstr[1][0], onInstr[1][1], offInstr[1][0], offInstr[1][1])
    newZDim = adaptOneDimensionOnOff(onInstr[2][0], onInstr[2][1], offInstr[2][0], offInstr[2][1])

    for xDim in newXDim:
        for yDim in newYDim:
            for zDim in newZDim:
                newSet = []
                newSet.append(xDim)
                newSet.append(yDim)
                newSet.append(zDim)
                newSet.append("on")
                allNewSets.append(newSet)

    return allNewSets


def adaptOnOnInstruction(onInstr, offInstr):
    allNewSets = []
    newXDim = adaptOneDimensionOnOn(onInstr[0][0], onInstr[0][1], offInstr[0][0], offInstr[0][1])
    newYDim = adaptOneDimensionOnOn(onInstr[1][0], onInstr[1][1], offInstr[1][0], offInstr[1][1])
    newZDim = adaptOneDimensionOnOn(onInstr[2][0], onInstr[2][1], offInstr[2][0], offInstr[2][1])

    for xDim in newXDim:
        for yDim in newYDim:
            for zDim in newZDim:
                newSet = []
                newSet.append(xDim)
                newSet.append(yDim)
                newSet.append(zDim)
                newSet.append("on")
                allNewSets.append(newSet)

    return allNewSets


instructions = []
xMinTotal = 0
xMaxTotal = 0
yMinTotal = 0
yMaxTotal = 0
zMinTotal = 0
zMaxTotal = 0

with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line)
    match = re.search("(.*) x=(.*)\.\.(.*),y=(.*)\.\.(.*),z=(.*)\.\.(.*)", line)
    instructionType = match.group(1)
    xMin = int(match.group(2))
    xMax = int(match.group(3))
    yMin = int(match.group(4))
    yMax = int(match.group(5))
    zMin = int(match.group(6))
    zMax = int(match.group(7))

    instructions.append([(xMin, xMax), (yMin, yMax), (zMin, zMax), instructionType])


for idx, instr in enumerate(instructions):
    if instr[3] == "off":
        for onInstrCnt in range(idx):
            if instructions[onInstrCnt][3] == "on":
                onInstr = instructions[onInstrCnt]
                offInstr = instr
                if doTwoInstructionOverlap(onInstr, offInstr):
                    adaptedInstrs = adaptOnOffInstruction(onInstr, offInstr)
                    first = True
                    for adaptedInstr in adaptedInstrs:
                        if first:
                            instructions[onInstrCnt] = adaptedInstr
                            first = False
                        else:
                            instructions.insert(0, adaptedInstr)


onCnt = 0
for onInstr in instructions:
    if onInstr == [] or onInstr[3] != "on":
        continue
    else:
        xRange = onInstr[0][1] - onInstr[0][0]
        yRange = onInstr[1][1] - onInstr[1][0]
        zRange = onInstr[2][1] - onInstr[2][0]

        onCnt += (xRange * yRange * zRange)




print(onCnt)
print("Done")

# exp: 
# 2758514936282235
# cal: 
# 1693556448840787