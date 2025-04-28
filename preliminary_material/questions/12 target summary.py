# # #

# Display a summary of the targets that were achieved, and how, at the end of the game.

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber):
    FinishedNumbers = []
    Score = 0
    GameOver = False
    while not GameOver:
        DisplayState(Targets, NumbersAllowed, Score)
        UserInput = input("Enter an expression: ")
        print()
        if CheckIfUserInputValid(UserInput):
            UserInputInRPN = ConvertToRPN(UserInput)
            if CheckNumbersUsedAreAllInNumbersAllowed(NumbersAllowed, UserInputInRPN, MaxNumber):
                # Update to get new variables
                IsTarget, Score, Target, NumberRemoved = CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score)
                if IsTarget:
                    NumbersAllowed = RemoveNumbersUsed(UserInput, MaxNumber, NumbersAllowed)
                    NumbersAllowed = FillNumbers(NumbersAllowed, TrainingGame, MaxNumber)
                    # Add UserInput and Target to array
                    for Index in range(NumberRemoved):
                        FinishedNumbers.append([UserInput, Target])
        Score -= 1

        if Targets[0] != -1:
            GameOver = True
            DisplaySummary(FinishedNumbers)
        else:
            Targets = UpdateTargets(Targets, TrainingGame, MaxTarget)
    print("Game over!")
    DisplayScore(Score)

def DisplaySummary(Numbers):
    # Print summary of targets
    print('Numbers achieved:')
    for Number in Numbers:
        print(f'{Number[0]} | {Number[1]}')

def CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score):
    UserInputEvaluation = EvaluateRPN(UserInputInRPN)
    UserInputEvaluationIsATarget = False
    NumberRemoved = 0
    if UserInputEvaluation != -1:
        for Count in range(0, len(Targets)):
            if Targets[Count] == UserInputEvaluation:
                Score += 2
                Targets[Count] = -1
                NumberRemoved += 1
                UserInputEvaluationIsATarget = True

    # Return Target and number of Targets removed
    return UserInputEvaluationIsATarget, Score, UserInputEvaluation, NumberRemoved

# # #