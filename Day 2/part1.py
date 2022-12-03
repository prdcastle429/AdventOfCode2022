playerScore = 0

with open("input.txt") as file:
    lines = file.readlines()

    for i in range(0, len(lines)):
        lineArr = lines[i].split(" ")
        oppChoice = lineArr[0]
        playerChoice = lineArr[1].strip()
        oppChoiceInt = ord(oppChoice) - 64
        playerChoiceInt = ord(playerChoice) - 87

        if oppChoiceInt == playerChoiceInt:
            playerScore += playerChoiceInt + 3

        elif playerChoiceInt - oppChoiceInt == 1 or playerChoiceInt - oppChoiceInt == -2:
            playerScore += playerChoiceInt + 6

        else:
            playerScore += playerChoiceInt

print(str(playerScore))