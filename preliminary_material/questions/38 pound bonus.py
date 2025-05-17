# # #

# When a target is cleared, put a £ symbol in its position in the target list. When the £ symbol reaches the end of the tracker, increase the score by 1

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber):
    Score = 0
    GameOver = False
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

        # Add score
        if Targets[0] == '£':
            Score += 1
        # If neither '£' or '-1', must be number, break game loop
        elif Targets[0] != -1:
            GameOver = True
            break
        Targets = UpdateTargets(Targets, TrainingGame, MaxTarget)

    print("Game over!")
    DisplayScore(Score)

def CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score):
    UserInputEvaluation = EvaluateRPN(UserInputInRPN)
    UserInputEvaluationIsATarget = False
    if UserInputEvaluation != -1:
        for Count in range(0, len(Targets)):
            if Targets[Count] == UserInputEvaluation:
                Score += 2
                # Change to '£' instead of '-1'
                Targets[Count] = '£'
                UserInputEvaluationIsATarget = True
    return UserInputEvaluationIsATarget, Score

# # #