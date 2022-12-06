import re

groups = [[]]
operations = []
finalString = ""

with open("input.txt") as file:
    lines = file.readlines()
    numGroups = lines.index("\n")
    columnIndex = 1
    for j in range(0, numGroups):
        currColumn = []
        for i in range(0, numGroups):
            if columnIndex < len(lines[i]) and lines[i][columnIndex].isalpha():
                currColumn.append(lines[i][columnIndex])
        columnIndex += 4
        currColumn.reverse()
        groups.append(currColumn)

    for i in range(numGroups + 1, len(lines)):
        newLine = re.sub('\D', ' ', lines[i])
        operation = list(map(int, newLine.split(None)))
        operations.append(operation)

for operation in operations:
    amountMoved = operation[0]
    fromGroup = groups[operation[1]]
    toGroup = groups[operation[2]]

    for i in range(0, amountMoved):
        crateMoved = fromGroup.pop()
        toGroup.append(crateMoved)

    groups[operation[1]] = fromGroup
    groups[operation[2]] = toGroup

for group in groups:
    if len(group) > 0:
        finalString += group[len(group) - 1]

print(finalString)
