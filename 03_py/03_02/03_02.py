import copy


def removeNumbers(numbers, index, excludingNumber):
    result = copy.deepcopy(numbers)
    for byte2 in numbers:
        if len(result) == 1:
            break
        if byte2[index] != excludingNumber:
            result.remove(byte2)

    return copy.deepcopy(result)


def calcDominantNumber(numbers, index, oneFlag):
    sumCo2 = 0
    totalNumberBytesC02 = len(numbers)
    for byte in numbers:
        sumCo2 += byte[index]

    if sumCo2 >= (totalNumberBytesC02/2):
        if oneFlag:
            dominantNumber = 1
        else:
            dominantNumber = 0
    else:
        if oneFlag:
            dominantNumber = 0
        else:
            dominantNumber = 1

    return dominantNumber


with open('input.txt') as f:
    lines = f.readlines()

allBytes = []

for line in lines:
    byte = []
    for bit in line.strip():
        byte.append(int(bit))
        
    allBytes.append(byte)

lengthByte = len(allBytes[0])

allBytesOxygen = copy.deepcopy(allBytes)
allBytesCO2 = copy.deepcopy(allBytes)

for byteIdx in range(lengthByte):
    dominantNumberOxy = ""
    dominantNumberCo2 = ""

    dominantNumberOxy = calcDominantNumber(allBytesOxygen, byteIdx, True)
    dominantNumberCo2 = calcDominantNumber(allBytesCO2, byteIdx, False)
    
    allBytesOxygen = removeNumbers(allBytesOxygen, byteIdx, dominantNumberOxy)
    allBytesCO2 = removeNumbers(allBytesCO2, byteIdx, dominantNumberCo2)

oxyResult = "".join(map(str, allBytesOxygen[0]))
co2Result = "".join(map(str, allBytesCO2[0]))

result = int(oxyResult, 2) * int(co2Result, 2)
print(result)

