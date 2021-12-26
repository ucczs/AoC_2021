import sys


def performExplosionTests():
    tests = [
        ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]", True),
        ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]", True),
        ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]", True),
        ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", True),
        ("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]", True),
        ("[[[[[1,1],[2,2]],[3,3]],[4,4]],[5,5]]", "[[[[3,0],[5,3]],[4,4]],[5,5]]", False),
        ("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]", "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", False)
    ]

    for idx, test in enumerate(tests):
        print("Start test: " + test[0])
        inputTest = ""
        result = test[0]
        while inputTest != result:
            if test[2]:
                inputTest = result
                result = explode(list(inputTest))
                break
            else:
                while inputTest != result:
                    inputTest = result
                    result = explode(list(inputTest))

            if not test[2]:
                result, _ = split(result)




        if test[1] != "".join(result):
            print("Incorrect behavior in test number " + str(idx) + ": " )
            print("Exp: " + test[1])
            print("Cal: " + "".join(result))
            sys.exit()
        else:
            print("Success: " + test[0] + " -> " + "".join(result))

    print("Test ended " + "*" * 30)


def explode(line):
    openCnt = 0

    explosionIdx = 0
    explosionVal1 = None
    explosionVal2 = None

    prevNumberStr = ""
    prevNumberIdx = None
    prevNumber = None

    followingNumberStr = ""
    follwingNumberIdx = None
    followingNumberIdx = None

    for idx, c in enumerate(line):
        if c == "[": 
            openCnt += 1
            if openCnt < 5:
                prevNumberStr = ""
        elif c == "]": 
            openCnt -= 1
            prevNumber = prevNumber if prevNumberStr == "" else int(prevNumberStr)
        elif c == ",":
            if explosionVal1 == None:
                prevNumber = prevNumber if prevNumberStr == "" else int(prevNumberStr)
        elif openCnt < 5 and explosionVal1 == None:
            prevNumberIdx = idx
            prevNumberStr = c
        elif openCnt == 5 and explosionVal1 == None: 
            explosionIdx = idx
            explosionVal1 = c
        elif openCnt == 5 and explosionVal2 == None:
            explosionVal2 = c
        elif explosionVal2 != None:
            followingNumberIdx = idx
            followingNumberStr = c
            break

    if explosionVal1 != None and explosionVal2 != None:
        if explosionVal1 != None and prevNumberIdx != None:
            val = prevNumber + int(explosionVal1)
            line = line[:prevNumberIdx] + [str(val)] + line[prevNumberIdx+1:]
        if followingNumberIdx != None:
            val = int(line[followingNumberIdx]) + int(explosionVal2)
            line = line[:followingNumberIdx] + [str(val)] + line[followingNumberIdx+1:]
        line = line[:explosionIdx-1] + ["0"] + line[explosionIdx:]
        line = line[:explosionIdx+3] + line[explosionIdx+4:]
        line = line[:explosionIdx+2] + line[explosionIdx+3:]
        line = line[:explosionIdx+1] + line[explosionIdx+2:]
        line = line[:explosionIdx+0] + line[explosionIdx+1:]

    return line


def performSplit(line, splitIdx):
    number = int(line[splitIdx])
    replacementStr = ["["] + [str(int(number/2))] + [","] + [str(int((number+1)/2))] + ["]"]
    line = line[:splitIdx] + replacementStr + line[splitIdx+1:]
    return line


def split(line):
    splitPerformed = False
    for idx, c in enumerate(line):
        if c not in ["[", "]", ","] and int(c) >= 10:
            line = performSplit(line, idx)
            splitPerformed = True
            break

    return line, splitPerformed


def calcMagnitude(processedInput):
    changed = True
    resultList = processedInput


    while(len(resultList) != 1):
        listtemp = []
        calculated = False

        for idx, c in enumerate(resultList):
            if not calculated:
                listtemp.append(c)
            elif c == "]":
                calculated = False
            if c == ",":
                if (resultList[idx-1].isnumeric() and
                    resultList[idx+1].isnumeric()):
                    result = int(resultList[idx-1]) * 3 + int(resultList[idx+1]) * 2
                    calculated = True
                    listtemp = listtemp[:-3]
                    listtemp.append(str(result))

        resultList = listtemp

    return(int(resultList[0]))




performExplosionTests()

with open('input.txt') as f:
    lines = f.readlines()

firstLine = True
mergedLines = ""
for line in lines:
    line = list(line.strip())
    if firstLine:
        mergedLines = line
        firstLine = False
    else:
        mergedLines = ["["] + mergedLines + [","] + line + ["]"]

    splitPerformed = True
    while(splitPerformed):
        lineExplode = mergedLines
        prevLine = ""
        while(prevLine != lineExplode):
            prevLine = lineExplode
            lineExplode = explode(list(prevLine))

        mergedLines, splitPerformed = split(lineExplode)

result = calcMagnitude(mergedLines)

print(result)
