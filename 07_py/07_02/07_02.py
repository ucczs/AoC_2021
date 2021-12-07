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
        fuelSum += int(abs(pos-i) * (abs(pos-i)+1) / 2)

    minFuel = min(minFuel, fuelSum)

print(minFuel)
print("Done")
