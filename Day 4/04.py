totalContainedPairs = 0
totalOverlappingPairs = 0

with open("input.txt") as file:
    lines = file.readlines();
    for line in lines:
        pairs = line.split(",")
        pairOne, pairTwo = list(map(int, pairs[0].split("-"))), list(map(int, pairs[1].split("-")))

        if (pairOne[0] >= pairTwo[0] and pairOne[1] <= pairTwo[1]) or (pairTwo[0] >= pairOne[0] and pairTwo[1] <= pairOne[1]):
            totalContainedPairs += 1

        if pairOne[1] in range(pairTwo[0], pairTwo[1] + 1) or pairTwo[1] in range(pairOne[0], pairOne[1] + 1):
            totalOverlappingPairs += 1

print("Total Contained Pairs: " + str(totalContainedPairs))
print("Total Overlapping Pairs: " + str(totalOverlappingPairs))
