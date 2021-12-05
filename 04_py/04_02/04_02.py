import copy

BOARD_SIZE = 5

def checkForBingo(grid):
    bingo = False
    for row in grid:
        if sum(row) == BOARD_SIZE:
            bingo = True

    for column in range(BOARD_SIZE):
        sumColumn = 0
        for row in grid:
            sumColumn += row[column]

        if sumColumn == BOARD_SIZE:
            bingo = True

    return bingo


def drawNextNumber(number, boards, matchGrids):
    for idx, board in enumerate(boards):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == number:
                    matchGrids[idx][i][j] = 1


def countResult(matchGrid, board, lastNumber):
    result = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if matchGrid[i][j] == 0:
                result += int(board[i][j])

    result = result * int(lastNumber)
    return result


with open('input.txt') as f:
    lines = f.readlines()

gameSteps = []
boards = []
board = []
matchGrids = []

for line in lines:
    if line == "\n" and board != [] and gameSteps != []:
        boards.append(copy.deepcopy(board))
        board = []

    if line.find(",") >= 0:
        gameSteps = line.split(",")

    if line != "" and line != "\n" and line.find(",") == -1:
        board.append(line.strip().replace("  ", " ").replace("\n", "").split(" "))

boards.append(copy.deepcopy(board))

matchGrid = [[0 for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

for i in range(len(boards)):
    matchGrids.append(copy.deepcopy(matchGrid))

for nextNumber in gameSteps:
    bingo = False
    drawNextNumber(nextNumber, boards, matchGrids)

    for idx, matchGrid in enumerate(matchGrids):
        if checkForBingo(matchGrid):
            result = countResult(matchGrid, boards[idx], nextNumber)
            if len(matchGrids) > 1:
                del matchGrids[idx]
                del boards[idx]
            else:
                print("Last bingo!")
                print(result)
                bingo = True
                break

    if bingo:
        break

