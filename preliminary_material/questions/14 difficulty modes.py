# # #

# Implement "easy" and "hard" modes, in which the target range is adjusted.

def Main():
    NumbersAllowed = []
    Targets = []
    MaxNumberOfTargets = 20
    MaxTarget = 0
    MaxNumber = 0
    TrainingGame = False
    Choice = input("Enter y to play the training game, anything else to play a random game: ").lower()
    print()
    Difficulty = input("Enter e for easy difficulty, or enter h for hard difficult: ").lower()
    print()
    if Choice == "y":
        if Difficulty == "e":
            MaxNumber = 1000
            MaxTarget = 1000
        else:
            MaxNumber = 100
            MaxTarget = 10000
        TrainingGame = True
        Targets = [-1, -1, -1, -1, -1, 23, 9, 140, 82, 121, 34, 45, 68, 75, 34, 23, 119, 43, 23, 119]
    else:
        if Difficulty == "e":
            MaxNumber = 10
            MaxTarget = 50
        else:
            MaxNumber = 5
            MaxTarget = 100
        Targets = CreateTargets(MaxNumberOfTargets, MaxTarget)
    NumbersAllowed = FillNumbers(NumbersAllowed, TrainingGame, MaxNumber)
    PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber)
    input()

# # #