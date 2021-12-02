with open('input.txt') as f:
    lines = f.readlines()

commands = []

for line in lines:
    command = line.split(" ")
    commands.append([command[0], int(command[1])])

horizontalPos = 0
depthPos = 0

for command in commands:
    if command[0] == "forward":
        horizontalPos += command[1]
    elif command[0] == "down":
        depthPos += command[1]
    elif command[0] == "up":
        depthPos -= command[1]
    else:
        print("Error command!")

result = horizontalPos * depthPos
print(result)
