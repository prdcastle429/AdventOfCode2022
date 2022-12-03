elfCaloriesArray = []

with open("input.txt") as file:
    lines = file.readlines()
    currElfCalories = 0
    for i in range(0, len(lines)):
        if lines[i] == "\n":
            elfCaloriesArray.append(currElfCalories)
            currElfCalories = 0
        else:
            currElfCalories = currElfCalories + int(lines[i].strip("\n"))

# Print part 1 solution
elfCaloriesArray.sort()
print("Highest Calories: " + str(elfCaloriesArray[len(elfCaloriesArray) - 1]))

# Print part 2 solution
sumOfThreeHighest = elfCaloriesArray[-1] + elfCaloriesArray[-2] + elfCaloriesArray[-3]
print("Sum of three highest: " + str(sumOfThreeHighest))