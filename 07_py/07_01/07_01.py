with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line)
    positions = line.split(",")
    positions = list(map(int, positions))

max = max(positions)
minFuel = 100000000

for i in range(max):
    fuelSum = 0
    for pos in positions:
        fuelSum += abs(pos-i)

    minFuel = min(minFuel, fuelSum)

print(minFuel)
print("Done")
