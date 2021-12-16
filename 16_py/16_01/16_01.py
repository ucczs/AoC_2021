def parsePackage(binInput, versionCnt):
    version = int("".join(binInput[0:3]), 2)
    typeID = int("".join(binInput[3:6]), 2)

    versionCnt += version

    if typeID == 4:
        lastElement = False
        elementCnt = 0
        while(not lastElement):
            startIdx = 6 + 5 * elementCnt
            endIdx = startIdx + 5
            lastElement = "".join(binInput[startIdx:startIdx+1]) == "0"
            elementCnt += 1

        remainingBin = binInput[endIdx:]
    else:
        lengthID = int("".join(binInput[6:7]), 2)
        if lengthID == 0:
            totalLengthBin = "".join(binInput[8:22])
            totalLength = int(totalLengthBin, 2)
            subpackages = binInput[22:22+totalLength]
            while len(subpackages) > 7:
                subpackages, versionCnt = parsePackage(subpackages, versionCnt)
            remainingBin = binInput[22+totalLength:]
        elif lengthID == 1:
            numberSubpackages = int("".join(binInput[7:18]), 2)
            remainingBin = binInput[18:]
            for _ in range(numberSubpackages):
                remainingBin, versionCnt = parsePackage(remainingBin, versionCnt)

    return (remainingBin, versionCnt)

with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    hexInput = list(line.strip())

binInput = ""
for val in hexInput:
    binInput += bin(int(val, 16))[2:].zfill(4)

binInput = list(binInput)

versionCnt = 0
binInput, versionCnt = parsePackage(binInput, versionCnt)


print(versionCnt)