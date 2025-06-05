# # #

# Allow the program to not stop after 'Game Over!' with no way for the user to exit.

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber):
    Score = 0
    GameOver = False
    # Make copy of starting variables, Targets[::] to create a fresh copy of the Targets list
    ArgumentsCopy = [Score, Targets[::], NumbersAllowed, TrainingGame, MaxTarget, MaxNumber]

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
        Score -= 1
        if Targets[0] != -1:
            GameOver = True
        else:
            Targets = UpdateTargets(Targets, TrainingGame, MaxTarget)

        if GameOver and input('Game Over! Enter r to restart, anything else to quit: ').lower() == 'r':
            GameOver = False
            # Reset variables and continue loop
            Score, Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber = ArgumentsCopy

    print("Game over!")
    DisplayScore(Score)

# # #