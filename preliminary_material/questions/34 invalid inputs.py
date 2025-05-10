# # #

# Do not advance the target list forward for invalid entries, instead inform the user the entry was invalid and prompt them for a new one

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber):
    Score = 0
    GameOver = False
    while not GameOver:
        DisplayState(Targets, NumbersAllowed, Score)

        # Keep looping until valid UserInput entered
        while not CheckIfUserInputValid(UserInput := input("Enter an expression: ")):
            print()
            print('Invalid input!')
            print()
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

# # #