# # #

# Allow the user to choose the NumbersAllowed. They would have to be fixed for that game I think.

def Main():
    NumbersAllowed = []
    Targets = []
    MaxNumberOfTargets = 20
    MaxTarget = 0
    MaxNumber = 0
    TrainingGame = False
    Choice = input("Enter y to play the training game, anything else to play a random game: ").lower()
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

    # Choose CustomNumberss
    ChooseNumber = input("Press y to choose own allowed numbers, anything else for randomly generated allowed numbers: ").lower()
    CustomNumbers = False
    print()
    if ChooseNumber == "y":
        NumbersAllowed = ChooseNumbers(NumbersAllowed, MaxNumber)
        CustomNumbers = True
    else:
        NumbersAllowed = FillNumbers(NumbersAllowed, TrainingGame, MaxNumber)
        CustomNumbers = False
    # Pass CustomNumbers option to main game
    PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber, CustomNumbers)
    input()

# Take CustomNumbers parameter
def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber, CustomNumbers):
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
                    # Pass CustomNumbers argument
                    NumbersAllowed = FillNumbers(NumbersAllowed, TrainingGame, MaxNumber, CustomNumbers)
        Score -= 1
        if Targets[0] != -1:
            GameOver = True
        else:
            Targets = UpdateTargets(Targets, TrainingGame, MaxTarget)
    print("Game over!")
    DisplayScore(Score)

# Accept CustomNumbers parameter
def FillNumbers(NumbersAllowed, TrainingGame, MaxNumber, CustomNumbers):
    # Only return preset allowed numbers preset if not using custom allowed numbers
    if TrainingGame and not CustomNumbers:
        return [2, 3, 2, 8, 512]
    else:
        while len(NumbersAllowed) < 5:
            NumbersAllowed.append(GetNumber(MaxNumber))
        return NumbersAllowed

# # #