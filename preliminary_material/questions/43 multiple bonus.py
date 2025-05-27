# # #

# Multiple of X. The program should randomly generate a number each turn, e.g. 3 and if the user creates an expression which removes a target which is a multiple of that number, give them a bonus of their score equal to the multiple (in this case, 3 extra score)

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber):
    Score = 0
    GameOver = False
    while not GameOver:
        DisplayState(Targets, NumbersAllowed, Score)

        # Create random multipler
        Multiplier = random.randint(1, 10)
        print(f"Your factor target for a bonus is: {Multiplier}")

        UserInput = input("Enter an expression: ")
        print()
        if CheckIfUserInputValid(UserInput):
            UserInputInRPN = ConvertToRPN(UserInput)
            if CheckNumbersUsedAreAllInNumbersAllowed(NumbersAllowed, UserInputInRPN, MaxNumber):
                # Pass Multipler as argument
                IsTarget, Score = CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score, Multiplier)
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

# Receive Multiplier parameter
def CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score, Multiplier):
    UserInputEvaluation = EvaluateRPN(UserInputInRPN)
    UserInputEvaluationIsATarget = False
    if UserInputEvaluation != -1:
        for Count in range(0, len(Targets)):
            if Targets[Count] == UserInputEvaluation:

                # If UserInputEvaluationIsATarget is False, firs time encountering in Targets so only runs once, and Multiplier is a factor of the target, increase score
                if UserInputEvaluationIsATarget is False and Targets[Count] % Multiplier == 0:
                    Score += Multiplier

                Score += 2
                Targets[Count] = -1
                UserInputEvaluationIsATarget = True
    return UserInputEvaluationIsATarget, Score

# # #