import re
import copy

unique = [1, 4, 7, 8]
uniqueLen = [2, 4, 3, 7]

regex = "(\w*) (\w*) (\w*) (\w*) (\w*) (\w*) (\w*) (\w*) (\w*) (\w*) \| (\w*) (\w*) (\w*) (\w*)"

def doInverse(charsList):
    inverse = ["a", "b", "c", "d", "e", "f", "g"]
    for chars in charsList:
        for value in chars:
            if value in inverse:
                inverse.remove(value)

    return inverse


def findCommon(charList1, charList2):
    return list(set(charList1).intersection(charList2))


def findWithSpecificLength(allValues, length):
    chars = []
    for values in allValues:
        for value in values:
            if (len(value) == length):
                chars = sorted(list(value))
                break

    return chars

outputValues = []
inputValues = []

results = {"a": "x", 
           "b": "x",
           "c": "x",
           "d": "x",
           "e": "x",
           "f": "x",
           "g": "x"}

with open('input.txt') as f:
    lines = f.readlines()

sum = 0

for line in lines:
    outputValues = []
    inputValues = []
    allValues = []

    output = []
    input = []
    allValues = []
    matches = re.search(regex, line)

    for i in range(1, 11):
        input.append(matches.group(i))

    for j in range(11, 15):
        output.append(matches.group(j))

    outputValues.append(copy.deepcopy(output))
    inputValues.append(copy.deepcopy(input))

    allValues.append(copy.deepcopy(input))
    allValues.append(copy.deepcopy(output))

    chars1 = findWithSpecificLength(allValues, 2)
    chars4 = findWithSpecificLength(allValues, 4)
    chars4Inverted = doInverse(chars4)

    chars690 = []
    for values in allValues:
        for value in values:
            if (len(value) == 6):
                if sorted(list(value)) not in chars690:
                    chars690.append(sorted(list(value)))
            if len(chars690) == 3:
                break
    
    commonChars690 = findCommon(chars690[0], chars690[1])
    commonChars690 = findCommon(commonChars690, chars690[2])
    
    notInCommon690 = doInverse(commonChars690)
    cChar = findCommon(chars1, notInCommon690)[0]
    eChar = findCommon(notInCommon690, chars4Inverted)[0]

    for outValues in outputValues:
        singleValue = ""
        for outVal in outValues:
            if len(outVal) == 6 and (cChar in outVal) and (eChar in outVal):
                singleValue += "0"
            elif len(outVal) == 2:
                singleValue += "1"
            elif len(outVal) == 5  and (eChar in outVal):
                singleValue += "2"
            elif len(outVal) == 5  and (eChar not in outVal) and (cChar in outVal):
                singleValue += "3"
            elif len(outVal) == 4:
                singleValue += "4"
            elif len(outVal) == 5  and (cChar not in outVal):
                singleValue += "5"
            elif len(outVal) == 6  and (cChar not in outVal):
                singleValue += "6"
            elif len(outVal) == 3:
                singleValue += "7"
            elif len(outVal) == 7:
                singleValue += "8"
            elif len(outVal) == 6  and (eChar not in outVal):
                singleValue += "9"
        sum += int(singleValue)
        print(singleValue)

print(sum)
print("Done")

# a = diff(1, 7)

# e = diff(6, 9) and not in 1
# c = diff(6, 9) and in 1

# number -> length
#        = rule to find
# 0 -> 6
#   = len(6) and c and e
# 1 -> 2 unique
#   = easy
# 2 -> 5
#   = len(5) and e
# 3 -> 5
#   = len(5) and not e and c
# 4 -> 4 unique
#   = easy
# 5 -> 5
#   = len(5) and not c
# 6 -> 6
#   = len(6) and not c
# 7 -> 3 unique
#   = easy
# 8 -> 7 unique
#   = easy
# 9 -> 6
#   = len(6) and not e

