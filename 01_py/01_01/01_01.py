with open('input.txt') as f:
    lines = f.readlines()

first = True
count = 0
for line in lines:
    if first:
        lastNumber = int(line)
        first = False
    else:
        if lastNumber < int(line):
            count += 1

        lastNumber = int(line)

print(count)

