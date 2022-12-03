totalValue = 0

with open("input.txt") as file:
    lines = file.readlines()
    groupOne = [lines[i] for i in range(0, len(lines)) if i % 3 == 0]
    groupTwo = [lines[i] for i in range(0, len(lines)) if i % 3 == 1]
    groupThree = [lines[i] for i in range(0, len(lines)) if i % 3 == 2]

    for i in range(0, len(groupOne)):
        sameChars = [char for char in groupOne[i] if char in groupTwo[i] and char in groupThree[i]]
        charValue = ord(sameChars[0]) - 96 if sameChars[0].islower() else ord(sameChars[0]) - 38
        totalValue += charValue

print("Total Value: " + str(totalValue))
