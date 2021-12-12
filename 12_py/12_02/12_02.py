import re

class Node:
    def __init__(self, name, big, start, end):
        self.neightbours = []
        self.name = name
        self.big = big
        self.start = start
        self.end = end

    def addNeightbour(self, newNeightbour):
        self.neightbours.append(newNeightbour)

class CaveSystem:
    def __init__(self):
        self.caveMap = []
        self.paths = []
        self.smallNodesCnt = 0

    def countSmallNodes(self):
        for node in self.caveMap:
            if not node.big:
                self.smallNodesCnt += 1

    def getNthSmallval(self, n):
        count = 0
        result = ""
        for node in self.caveMap:
            if not node.big and not node.start and not node.end:
                count += 1
                if count == n:
                    result = node.name
                    break
        return result

    def getNode(self, nodeName):
        foundNode = None
        for node in self.caveMap:
            if node.name == nodeName:
                foundNode = node
                break
        return foundNode

    def addNode(self, newNode):
        self.caveMap.append(newNode)

    def addPair(self, node1, node2):
        for node in [node1, node2]:
            existingNode = self.getNode(node)

            if existingNode == None:
                big = True if (ord(node[0]) < 96) else False
                start = True if (node == "start") else False
                end = True if (node == "end") else False
                newNode = Node(node, big, start, end)
                self.addNode(newNode)

        node1Obj = self.getNode(node1)
        node2Obj = self.getNode(node2)

        node1Obj.addNeightbour(node2Obj)
        node2Obj.addNeightbour(node1Obj)


caveSystem = CaveSystem()

with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line)

    match = re.search("(.*)-(.*)", line)
    node1 = match.group(1)
    node2 = match.group(2)
    caveSystem.addPair(node1, node2)

caveSystem.countSmallNodes()

result = 0
pathsStrings = []

for i in range(caveSystem.smallNodesCnt):
    jokerNode = caveSystem.getNthSmallval(i+1)

    allPathsFound = False
    paths = ["start"]

    while(not allPathsFound):
        allPathsFound = True
        newPaths = []
        for path in paths:
            lastNodeString = path.split(",")[-1]
            if lastNodeString == "end":
                newPaths.append(path)
                continue

            lastNode = caveSystem.getNode(lastNodeString)
            for neightbour in lastNode.neightbours:
                if neightbour.name == "start":
                    continue

                smallVal = ord(neightbour.name[0]) > 96
                numberOfOccurance = path.count(neightbour.name)
                isNodeJoker = (neightbour.name == jokerNode)
                if isNodeJoker:
                    tooOften = True if numberOfOccurance >= 2 else False
                else:
                    tooOften = True if numberOfOccurance >= 1 else False

                if smallVal and tooOften:
                    continue
                else:
                    allPathsFound = False
                    nextPath = path + "," + neightbour.name
                    newPaths.append(nextPath)

        paths = newPaths

    pathsStrings = pathsStrings + paths

pathsStrings = list(dict.fromkeys(pathsStrings))
print(len(pathsStrings))
