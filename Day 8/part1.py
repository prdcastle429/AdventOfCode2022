gridArr = []
numVisibleTrees = 0

with open("input.txt") as file:
    lines = file.readlines()
    numVisibleTrees += 2 * len(lines) + 2 * (len(lines[0].strip()) - 2)
    for line in lines:
        line = line.strip()
        line = [int(num) for num in line]
        gridArr.append(line)

for i in range(1, len(gridArr) - 1):
    for j in range(1, len(gridArr[0]) - 1):
        treesToLeft = gridArr[i][0:j]
        treesToRight = gridArr[i][j+1:len(gridArr[i])]
        treesAbove = [gridArr[x][j] for x in range(0, i)]
        treesBelow = [gridArr[x][j] for x in range(i+1, len(gridArr))]

        biggerTreesLeft = [tree for tree in treesToLeft if tree >= gridArr[i][j]]
        biggerTreesRight = [tree for tree in treesToRight if tree >= gridArr[i][j]]
        biggerTreesAbove = [tree for tree in treesAbove if tree >= gridArr[i][j]]
        biggerTreesBelow = [tree for tree in treesBelow if tree >= gridArr[i][j]]

        if len(biggerTreesLeft) == 0 or len(biggerTreesRight) == 0 or len(biggerTreesAbove) == 0 or len(biggerTreesBelow) == 0:
            numVisibleTrees += 1

print("Total Visible Trees: " + str(numVisibleTrees))
