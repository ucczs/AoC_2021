with open('input.txt') as f:
    lines = f.readlines()

allBytes = []

for line in lines:
    byte = []
    for bit in line.strip():
        byte.append(int(bit))
        
    allBytes.append(byte)

lengthByte = len(allBytes[0])
totalNumberBytes = len(allBytes)

resultGamma = ""
resultEpsilon = ""

for byteIdx in range(lengthByte):
    sum = 0
    for byte in allBytes:
        sum += byte[byteIdx]

    if sum > (totalNumberBytes/2):
        resultGamma += "1"
        resultEpsilon += "0"
    else:
        resultGamma += "0"
        resultEpsilon += "1"

result = int(resultGamma,2) * int(resultEpsilon,2)
print(result)





