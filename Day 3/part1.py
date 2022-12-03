totalValue = 0

with open("input.txt") as file:
    lines = file.readlines()
    for rucksack in lines:
        firstCompartment = rucksack[len(rucksack)//2:]
        secondCompartment = rucksack[:len(rucksack)//2]

        sameChars = [char for char in firstCompartment if char in secondCompartment]
        charValue = ord(sameChars[0]) - 96 if sameChars[0].islower() else ord(sameChars[0]) - 38
        totalValue += charValue

print("Total Value: " + str(totalValue))
