import copy

with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line)
    fishes = line.split(",")

fishes = list(map(int, fishes))

count_before = [fishes.count(x) for x in range(0,9)]
count_after = [0 for _ in range(0,9)]

for day in range(256):
    zeroCount = count_before[0]

    for i in range(0,8):
        count_after[i] = count_before[i+1]

    count_after[8] = zeroCount
    count_after[6] += zeroCount

    count_before = copy.deepcopy(count_after)

result = sum(count_before)
print(result)
