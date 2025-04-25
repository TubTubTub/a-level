# # #

# Something to do with the difference between MaxTarget and MaxNumber in the normal game and training game

import math

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber):
    Score = 0
    GameOver = False
    TempMaxNumber = MaxNumber
    TempMaxTarget = MaxTarget

    while not GameOver:
        DisplayState(Targets, NumbersAllowed, Score)
        UserInput = input("Enter an expression: ")
        print()
        if CheckIfUserInputValid(UserInput):
            UserInputInRPN = ConvertToRPN(UserInput)
            if CheckNumbersUsedAreAllInNumbersAllowed(NumbersAllowed, UserInputInRPN, MaxNumber):
                IsTarget, Score = CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score)
                if IsTarget:
                    NumbersAllowed = RemoveNumbersUsed(UserInput, MaxNumber, NumbersAllowed)
                    NumbersAllowed = FillNumbers(NumbersAllowed, TrainingGame, MaxNumber)

        # Scale MaxNumber and MaxTarget based on current score
        if Score >= 10 and TrainingGame is False:
            MaxNumber = math.ceil(TempMaxNumber * 0.5)
            MaxTarget = math.floor(TempMaxTarget * 1.5)
        elif Score >= 5 and TrainingGame is False:
            MaxNumber = math.ceil(TempMaxNumber * 0.8)
            MaxTarget = math.floor(TempMaxTarget * 1.2)
        else:
            MaxNumber = TempMaxNumber
            MaxTarget = TempMaxTarget

        Score -= 1
        if Targets[0] != -1:
            GameOver = True
        else:
            Targets = UpdateTargets(Targets, TrainingGame, MaxTarget)
    print("Game over!")
    DisplayScore(Score)