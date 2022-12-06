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
        groups.append(currColumn)

    for i in range(numGroups + 1, len(lines)):
        newLine = re.sub('\D', ' ', lines[i])
        operation = list(map(int, newLine.split(None)))
        operations.append(operation)


for operation in operations:
    amountMoved = operation[0]
    fromGroup = groups[operation[1]]
    toGroup = groups[operation[2]]
    cratesToMove = fromGroup[:amountMoved]
    newToGroup = cratesToMove + toGroup
    newFromGroup = fromGroup[amountMoved:]

    groups[operation[1]] = newFromGroup
    groups[operation[2]] = newToGroup

for group in groups:
    if len(group) > 0:
        finalString += group[0]

print(finalString)