# # #

# For a small points cost, regenerate the NumbersAllowed or eliminate a particular target number.

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber):
    Score = 0
    GameOver = False
    while not GameOver:
        DisplayState(Targets, NumbersAllowed, Score)
        UserInput = input("Enter an expression, or r to regenerate allowed numbers (1 point penalty): ")
        print()

        if UserInput == 'r' or UserInput == 'R':
            # Empty NumbersAllowed so FillNumbers can fill the array with completely new numbers
            NumbersAllowed = []
            NumbersAllowed = FillNumbers(NumbersAllowed, TrainingGame, MaxNumber)
            # Deduct one point
            Score -= 1
            continue
        
        if CheckIfUserInputValid(UserInput):
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

# # #