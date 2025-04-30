# # #

# Calculate and display game statistics.

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber):
    Score = 0
    # Initialise Rounds and HighestNumber stats
    Rounds = 0
    HighestNumber = 0
    GameOver = False
    while not GameOver:
        Rounds += 1
        DisplayState(Targets, NumbersAllowed, Score)
        UserInput = input("Enter an expression: ")
        print()
        if CheckIfUserInputValid(UserInput):
            UserInputInRPN = ConvertToRPN(UserInput)
            if CheckNumbersUsedAreAllInNumbersAllowed(NumbersAllowed, UserInputInRPN, MaxNumber):
                # Receive 0 or number evaluated from user input
                IsTarget, Score, UserValue = CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score)
                HighestNumber = max(HighestNumber, UserValue)
                if IsTarget:
                    NumbersAllowed = RemoveNumbersUsed(UserInput, MaxNumber, NumbersAllowed)
                    NumbersAllowed = FillNumbers(NumbersAllowed, TrainingGame, MaxNumber)
        Score -= 1
        if Targets[0] != -1:
            GameOver = True
        else:
            Targets = UpdateTargets(Targets, TrainingGame, MaxTarget)
    print("Game over!")
    # Pass Rounds and HighestNumber arguments
    DisplayScore(Score, Rounds, HighestNumber)

def CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score):
    UserInputEvaluation = EvaluateRPN(UserInputInRPN)
    UserInputEvaluationIsATarget = False
    if UserInputEvaluation != -1:
        for Count in range(0, len(Targets)):
            if Targets[Count] == UserInputEvaluation:
                Score += 2
                Targets[Count] = -1
                UserInputEvaluationIsATarget = True
    # Return UserInputEvaluation if in targets, else return 0
    return UserInputEvaluationIsATarget, Score, UserInputEvaluation if UserInputEvaluationIsATarget else 0

# Receive optional Rounds and HighestNumber parameters
def DisplayScore(Score, Rounds=None, HighestNumber=None):
    print("Current score: " + str(Score))
    print()
    if Rounds is not None:
        print("Number of rounds: " + str(Rounds))
        print()
    if HighestNumber is not None:
        print("Highest number achieved: " + str(HighestNumber))
        print()

# # #