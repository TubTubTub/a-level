# # #

# Add the ability to clear any target

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber):
    Score = 0
    GameOver = False
    while not GameOver:
        DisplayState(Targets, NumbersAllowed, Score)

        # Only allow free clearing if in TrainingGame mode
        if TrainingGame:
            UserInput = input("Enter an expression (x for free clear): ")
            print()

            if UserInput == 'x':
                NumberToClear = int(input("Enter number to clear: "))
                print()

                # Replaces all selected number in Targets with -1
                Targets = [-1 if x == NumberToClear else x for x in Targets]
                # Skip to next loop, score not increased for free clears
                continue
        else:
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
    print("Game over!")
    DisplayScore(Score)

# # #