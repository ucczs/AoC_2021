import re
import copy

class Node:
    def __init__(self, name, big, start, end, visited):
        self.neightbours = []
        self.name = name
        self.big = big
        self.start = start
        self.end = end
        self.visited = visited
        self.visitedTwice = True
        self.deadEnd = False

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

    def setNthJoker(self, n):
        count = 0
        for node in self.caveMap:
            if not node.big:
                count += 1
                if count == n:
                    node.visitedTwice = False

    def findDeadEnds(self):
        for node in self.caveMap:
            node.deadEnd = len(node.neightbours) == 1 and node.neightbours[0].big == False

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
        existingNode1 = self.getNode(node1)
        existingNode2 = self.getNode(node2)

        if existingNode1 == None:
            big = True if (ord(node1[0]) < 96) else False
            start = True if (node1 == "start") else False
            end = True if (node1 == "end") else False
            newNode1 = Node(node1, big, start, end, False)
            self.addNode(newNode1)

        if existingNode2 == None:
            big = True if (ord(node2[0]) < 96) else False
            start = True if (node2 == "start") else False
            end = True if (node2 == "end") else False
            newNode2 = Node(node2, big, start, end, False)
            self.addNode(newNode2)

        node1Obj = self.getNode(node1)
        node2Obj = self.getNode(node2)

        node1Obj.addNeightbour(node2Obj)
        node2Obj.addNeightbour(node1Obj)

    def getNodeByName(self, name):
        startNode = None
        for node in self.caveMap:
            if node.name == name:
                startNode = node
                break
        return startNode

    def getStartNode(self):
        return self.getNodeByName("start")

    def getEndNode(self):
        return self.getNodeByName("end")


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
    jokerCaveSystem = copy.deepcopy(caveSystem)
    jokerCaveSystem.setNthJoker(i+1)
    startNode = jokerCaveSystem.getStartNode()

    allPathsFound = False
    paths = [[startNode]]

    while(not allPathsFound):
        allPathsFound = True
        newPaths = []
        for path in paths:
            lastNode = path[-1]
            if lastNode.name == "end":
                newPaths.append(path)
                continue
            for neightbour in lastNode.neightbours:
                if neightbour.name == "start":
                    continue
                elif neightbour.visited and neightbour.visitedTwice and not neightbour.big:
                    continue
                else:
                    allPathsFound = False
                    newPath = copy.deepcopy(path)
                    neightbourPath = copy.deepcopy(neightbour)
                    if neightbourPath.visited:
                        neightbourPath.visitedTwice = True
                    else:
                        neightbourPath.visited = True
                    newPath.append(neightbourPath)
                    newPaths.append(newPath)

        paths = newPaths

    for path in paths:
        pathString = ""
        for node in path:
            pathString += (node.name + ",")
        pathsStrings.append(pathString[:-1])

pathsStrings = list(dict.fromkeys(pathsStrings))
print(len(pathsStrings))
print("Done")
