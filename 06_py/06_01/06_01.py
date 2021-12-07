with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line)
    fishes = line.split(",")

fishes = list(map(int, fishes))


for i in range(80):
    appendCounter = 0
    for idx, fish in enumerate(fishes):
        if fishes[idx] == 0:
            fishes[idx] = 6
            appendCounter += 1
        else:
            fishes[idx] -= 1

    for j in range(appendCounter):
        fishes.append(8)

print(len(fishes))
print("Done")