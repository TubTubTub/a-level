# # #

# Implement a "streak" bonus.

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber):
    Streak = 0
    Score = 0
    GameOver = False
    while not GameOver:
        DisplayState(Targets, NumbersAllowed, Score)
        UserInput = input("Enter an expression: ")
        print()
        if CheckIfUserInputValid(UserInput):
            UserInputInRPN = ConvertToRPN(UserInput)
            if CheckNumbersUsedAreAllInNumbersAllowed(NumbersAllowed, UserInputInRPN, MaxNumber):
                # Pass streak
                IsTarget, Score = CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score, Streak)
                if IsTarget:
                    NumbersAllowed = RemoveNumbersUsed(UserInput, MaxNumber, NumbersAllowed)
                    NumbersAllowed = FillNumbers(NumbersAllowed, TrainingGame, MaxNumber)
                    Streak += 1
                else:
                    Streak = 0
            else:
                Streak = 0
        else:
            Streak = 0

        Score -= 1
        if Targets[0] != -1:
            GameOver = True
        else:
            Targets = UpdateTargets(Targets, TrainingGame, MaxTarget)
    print("Game over!")
    DisplayScore(Score)

def CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score, Streak):
    UserInputEvaluation = EvaluateRPN(UserInputInRPN)
    UserInputEvaluationIsATarget = False
    if UserInputEvaluation != -1:
        for Count in range(0, len(Targets)):
            if Targets[Count] == UserInputEvaluation:
                # Increase score depending on streak, (Streak + 1) to prevent multiplying by 0
                Score += 2 * (Streak + 1)
                Targets[Count] = -1
                UserInputEvaluationIsATarget = True
    return UserInputEvaluationIsATarget, Score

# # #