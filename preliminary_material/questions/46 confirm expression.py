# # #

# Validate a user's entry to confirm their choice before accepting an expression

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber):
    Score = 0
    GameOver = False
    while not GameOver:
        DisplayState(Targets, NumbersAllowed, Score)
        UserInput = input("Enter an expression: ")
        print()
        if CheckIfUserInputValid(UserInput):

            # Confirm UserInput, reset loop if UserInput is not 'y'
            Confirm = input(f"Press y to confirm the following expression ({UserInput}): ")
            print()
            if Confirm.lower() != "y":
                continue

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