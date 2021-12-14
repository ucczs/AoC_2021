import re
import copy

with open('input.txt') as f:
    lines = f.readlines()

rule = {}
template = []
for line in lines:
    print(line)
    if line.find("-") >= 0:
        match = re.search("(.*)->(.*)", line)
        pair = "".join(list(match.group(1).strip()))
        insert = match.group(2).strip()
        rule[pair] = insert
    elif line != "\n":
        template = line.strip()

countPair = {}
for i in range(len(template)-1):
    key = template[i]+template[i+1]
    if key not in countPair.keys():
        countPair[key] = 1
    else:
        countPair[key] += 1

for i in range(40):
    counterTemp = {}
    for k in countPair:
        key1 = k[0]+rule[k]
        key2 = rule[k]+k[1]

        for key in [key1, key2]:
            if key not in counterTemp.keys():
                counterTemp[key] = countPair[k]
            else:
                counterTemp[key] += countPair[k]

    countPair = counterTemp

counterResult = {}
for k in countPair.keys():
    if k[0] not in counterResult.keys():
        counterResult[k[0]] = countPair[k]
    else:
        counterResult[k[0]] += countPair[k]

counterResult[template[-1]] += 1

result = max(counterResult.values()) - min(counterResult.values())

print(result)