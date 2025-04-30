# # #

# Implement a mode in which the potential operators are limited, for instance + and - only.

def Main():
    NumbersAllowed = []
    Targets = []
    MaxNumberOfTargets = 20
    MaxTarget = 0
    MaxNumber = 0
    TrainingGame = False
    Choice = input("Enter y to play the training game, anything else to play a random game: ").lower()
    print()
    # Check if input is n
    NormalDifficulty = input("Enter n for normal difficulty, anything else for hard difficulty (+ or - operator only): ").lower() == "n"
    print()
    if Choice == "y":
        MaxNumber = 1000
        MaxTarget = 1000
        TrainingGame = True
        Targets = [-1, -1, -1, -1, -1, 23, 9, 140, 82, 121, 34, 45, 68, 75, 34, 23, 119, 43, 23, 119]
    else:
        MaxNumber = 10
        MaxTarget = 50
        Targets = CreateTargets(MaxNumberOfTargets, MaxTarget)
    NumbersAllowed = FillNumbers(NumbersAllowed, TrainingGame, MaxNumber)
    # Pass if NormalDifficulty argument
    PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber, NormalDifficulty)
    input()

# Receive NormalDifficulty parameter
def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber, NormalDifficulty):
    Score = 0
    GameOver = False
    while not GameOver:
        DisplayState(Targets, NumbersAllowed, Score)
        UserInput = input("Enter an expression: ")
        print()
        # Pass NormalDifficulty argument
        if CheckIfUserInputValid(UserInput, NormalDifficulty):
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

# Receive NormalDifficulty parameter
def CheckIfUserInputValid(UserInput, NormalDifficulty):
    if NormalDifficulty is True:
        if re.search("^([0-9]+[\\+\\-\\*\\/])+[0-9]+$", UserInput) is not None:
            return True
        else:
            return False
    else:
        # Only allow + and - operators for hard diffculty
        if re.search("^([0-9]+[\\+\\-])+[0-9]+$", UserInput) is not None:
            return True
        else:
            return False

# # #