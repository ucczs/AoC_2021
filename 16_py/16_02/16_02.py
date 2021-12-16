import math

def parsePackage(binInput):
    typeID = int("".join(binInput[3:6]), 2)

    if typeID == 4:
        value = ""
        lastElement = False
        elementCnt = 0
        while(not lastElement):
            startIdx = 6 + 5 * elementCnt
            endIdx = startIdx + 5
            value += "".join(binInput[startIdx+1:endIdx])
            lastElement = "".join(binInput[startIdx:startIdx+1]) == "0"
            elementCnt += 1
        finalVal = int(value, 2)

        remainingBin = binInput[endIdx:]
    else:
        result = []
        lengthID = int("".join(binInput[6:7]), 2)
        if lengthID == 0:
            totalLengthBin = "".join(binInput[8:22])
            totalLength = int(totalLengthBin, 2)
            subpackages = binInput[22:22+totalLength]
            while len(subpackages) > 7:
                subpackages, value = parsePackage(subpackages)
                result.append(value)
            remainingBin = binInput[22+totalLength:]
        elif lengthID == 1:
            numberSubpackages = int("".join(binInput[7:18]), 2)
            remainingBin = binInput[18:]
            for _ in range(numberSubpackages):
                remainingBin, value = parsePackage(remainingBin)
                result.append(value)

        if typeID == 0:
            finalVal = sum(result)
        elif typeID == 1:
            finalVal = math.prod(result)
        elif typeID == 2:
            finalVal = min(result)
        elif typeID == 3:
            finalVal = max(result)
        elif typeID == 5:
            finalVal = 1 if result[0] > result[1] else 0
        elif typeID == 6:
            finalVal = 1 if result[0] < result[1] else 0
        elif typeID == 7:
            finalVal = 1 if result[0] == result[1] else 0

    return remainingBin, finalVal


with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    hexInput = list(line.strip())

binInput = ""
for val in hexInput:
    binInput += bin(int(val, 16))[2:].zfill(4)

binInput = list(binInput)
binInput, result = parsePackage(binInput)

print(result)
