import re

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
        template = list(line.strip())


totalSteps = 10

for _ in range(totalSteps):
    output = ""
    for i in range(len(template)):
        output += template[i]

        if i < len(template)-1:
            ruleApply = "".join(list(template[i:i+2]))
            output += rule[ruleApply]

    template = list(output)


uniqueElements = set(template)
minCnt = 9999999
maxCnt = 0

for element in uniqueElements:
    cnt = template.count(element)
    minCnt = min(minCnt, cnt)
    maxCnt = max(maxCnt, cnt)

result = maxCnt - minCnt

print(result)
