# # #

# Different way of dealing with invalid input (instead of deducting marks) or implement some other way of enhancing input validation, such as detecting divide by zero errors, perhaps by handling ZeroDivisionError.

import re

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber):
    Score = 0
    GameOver = False
    while not GameOver:
        DisplayState(Targets, NumbersAllowed, Score)

        # Changed to loop until valid input entered
        while CheckIfUserInputValid(UserInput := input("Enter an expression: ")) is False:
            print('Invalid input!')
            print()

        UserInputInRPN = ConvertToRPN(UserInput)
        if CheckNumbersUsedAreAllInNumbersAllowed(NumbersAllowed, UserInputInRPN, MaxNumber):
            IsTarget, Score = CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score)
            if IsTarget:
                NumbersAllowed = RemoveNumbersUsed(UserInput, MaxNumber, NumbersAllowed)
                NumbersAllowed = FillNumbers(NumbersAllowed, TrainingGame, MaxNumber)

        Score -= 1
        if Targets[0] != -1:
            GameOver = True
        else:
            Targets = UpdateTargets(Targets, TrainingGame, MaxTarget)
    print("Game over!")
    DisplayScore(Score)

def CheckIfUserInputValid(UserInput):
    if re.search("^([0-9]+[\\+\\-\\*\\/\\^])+[0-9]+$", UserInput) is not None:
        # Find al / characters in string, if 0 after them return
        indexes = [i for i, item in enumerate(UserInput) if item == '/']

        for idx in indexes:
            if UserInput[idx + 1] == '0':
                return False
            
        return True
    
    return False

# # #