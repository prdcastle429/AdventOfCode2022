playerScore = 0

with open("input.txt") as file:
    lines = file.readlines()

    for i in range(0, len(lines)):
        lineArr = lines[i].split(" ")
        oppChoice = lineArr[0]
        playerChoice = lineArr[1].strip()
        oppChoiceInt = ord(oppChoice) - 64
        gameResultInt = ord(playerChoice) - 87

        if gameResultInt == 1:
            playerChoiceInt = oppChoiceInt - 1 if oppChoiceInt > 1 else 3
            playerScore += playerChoiceInt

        elif gameResultInt == 2:
            playerScore += oppChoiceInt + 3

        else:
            playerChoiceInt = oppChoiceInt + 1 if oppChoiceInt < 3 else 1
            playerScore += playerChoiceInt + 6

print(str(playerScore))