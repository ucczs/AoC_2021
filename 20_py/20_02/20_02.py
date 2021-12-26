import itertools

def extendInputImage(inputImage, count, symbol):
    for row in inputImage:
        for _ in range(count):
            row.insert(0, symbol)
            row.append(symbol)

    emptyRow = [symbol for _ in range(len(inputImage[0]))]
    for _ in range(count):
        inputImage.insert(0, emptyRow)
        inputImage.append(emptyRow)

    return inputImage

def printImage(image):
    for row in image:
        print(row)


def getSquareValue(image, basePos):
    combi = [[-1,0,1], [-1,0,1]]
    resultStr = ""
    for posOffset in itertools.product(*combi):
        position = (basePos[0] + posOffset[0], basePos[1] + posOffset[1])
        resultStr += image[position[0]][position[1]]

    result = int(resultStr.replace(".", "0").replace("#", "1"), 2)
    return result


def processImage(inputImage, algo):
    resultImage = [["." for _ in range(len(inputImage[0]))] for _ in range(len(inputImage))]
    for y in range(1,len(inputImage)-1):
        for x in range(1,len(inputImage[0])-1):
            value = getSquareValue(inputImage, (y,x))
            resultImage[y][x] = algo[value]

    return resultImage


def countLights(inputImage):
    count = 0
    for y in range(len(inputImage)):
        for x in range(len(inputImage[0])):
            if(inputImage[y][x] == "#"):
                count += 1
    return count


def replaceBorder(inputImage, symbol):
    for idx, row in enumerate(inputImage):
        if idx == 0 or idx == len(inputImage)-1:
            inputImage[idx] = [symbol for _ in range(len(inputImage[0]))]
        else:
            inputImage[idx][0] = symbol
            inputImage[idx][-1] = symbol

    return inputImage


with open('input.txt') as f:
    lines = f.readlines()

firstLine = True

imageAlgo = []
inputImage = []
for line in lines:
    print(line)
    if firstLine:
        imageAlgo = list(line.strip())
        firstLine = False
    else:
        if line == "\n":
            pass
        else:
            inputImage.append(list(line.strip()))

totalSteps = 50
for i in range(totalSteps):
    if imageAlgo[0] == ".":
        symbol = "."
    else:
        if i % 2 == 0:
            symbolExtended = "."
            symbolReplace = "#"
        else:
            symbolExtended = "#"
            symbolReplace = "."

    inputImage = extendInputImage(inputImage, 2, symbolExtended)
    inputImage = processImage(inputImage, imageAlgo)
    inputImage = replaceBorder(inputImage, symbolReplace)

result = countLights(inputImage)

print(result)
