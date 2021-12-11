def lineCorrupt(chars):
    corrupt = False
    openChar = []
    for c in chars:
        if c in openCharsColl:
            openChar.append(c)
        else:
            if matchingChars[openChar[-1]] == c:
                del openChar[-1]
            else:
                corrupt = True
                break

    return corrupt

with open('input.txt') as f:
    lines = f.readlines()

openCharsColl = ['(', '[', '{', '<']
matchingChars = {'(': ')', '[': ']', '{': '}', '<': '>'}

counting = {')': 1, ']': 2, '}': 3, '>': 4}

resultList = []
for line in lines:
    resultSingle = 0
    chars = list(line.strip())
    openChar = []
    if not lineCorrupt(chars):
            for c in chars:
                if c in openCharsColl:
                    openChar.append(c)
                else:
                    if matchingChars[openChar[-1]] == c:
                        del openChar[-1]

    if openChar != []:
        openChar.reverse()
        for c in openChar:
            missingChar = matchingChars[c]
            resultSingle *= 5
            resultSingle += counting[missingChar]

        resultList.append(resultSingle)

resultList = sorted(resultList)

resultIdx = int(len(resultList) / 2)
result = resultList[resultIdx]

print(result)

