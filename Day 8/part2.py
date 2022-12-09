gridArr = []
numVisibleTrees = 0
scenicScores = []

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

        nextBlockingTreeAbove = next((tree for tree in reversed(treesAbove) if tree >= gridArr[i][j]), -1)
        scenicScoreAbove = 0
        if nextBlockingTreeAbove != -1:
            lastMatchingIndex = len(treesAbove) - 1 - treesAbove[::-1].index(nextBlockingTreeAbove)
            scenicScoreAbove = i - lastMatchingIndex
        else:
            scenicScoreAbove = len(treesAbove)

        nextBlockingTreeBelow = next((tree for tree in treesBelow if tree >= gridArr[i][j]), -1)
        scenicScoreBelow = 0
        if nextBlockingTreeBelow != -1:
            lastMatchingIndex = treesBelow.index(nextBlockingTreeBelow)
            scenicScoreBelow = lastMatchingIndex + 1
        else:
            scenicScoreBelow = len(treesBelow)

        nextBlockingTreeLeft = next((tree for tree in reversed(treesToLeft) if tree >= gridArr[i][j]), -1)
        scenicScoreLeft = 0
        if nextBlockingTreeLeft != -1:
            lastMatchingIndex = len(treesToLeft) - 1 - treesToLeft[::-1].index(nextBlockingTreeLeft)
            scenicScoreLeft = j - lastMatchingIndex
        else:
            scenicScoreLeft = len(treesToLeft)

        nextBlockingTreeRight = next((tree for tree in treesToRight if tree >= gridArr[i][j]), -1)
        scenicScoreRight = 0
        if nextBlockingTreeRight != -1:
            lastMatchingIndex = treesToRight.index(nextBlockingTreeRight)
            scenicScoreRight = lastMatchingIndex + 1
        else:
            scenicScoreRight = len(treesToRight)
        scenicScore = scenicScoreLeft * scenicScoreRight * scenicScoreAbove * scenicScoreBelow
        scenicScores.append(scenicScore)

print("Largest Scenic Score: " + str(max(scenicScores)))