import re
import copy

unique = [(1, 2), (4, 4), (7, 3), (8, 7)]
uniqueLen = [2, 4, 3, 7]

regex = ".* \| (\w*) (\w*) (\w*) (\w*)"

outputValues = []

with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line)
    output = []
    matches = re.search(regex, line)
    output.append(len(matches.group(1)))
    output.append(len(matches.group(2)))
    output.append(len(matches.group(3)))
    output.append(len(matches.group(4)))

    outputValues.append(copy.deepcopy(output))

sum = 0
for output in outputValues:
    for val in output:
        if val in uniqueLen:
            sum += 1

print(sum)
print("Done")
