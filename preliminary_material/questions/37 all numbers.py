# # #

# If the user creates a qualifying expression which uses all the allowable numbers, grant the user a special reward ability (one use until unlocked again) to allow the user to enter any number of choice and this value will be removed from the target list

import re

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber):
    Score = 0
    GameOver = False
    AllNumbersUsed = False

    while not GameOver:
        DisplayState(Targets, NumbersAllowed, Score)
        # Disply new input message if destroy-any-target mode is on
        if AllNumbersUsed:
            UserInput = input('You used all available numbers! Enter any target to remove: ')
        else:
            UserInput = input("Enter an expression: ")
        print()

        # If in destroy-any-target mode, and inputted number is valid
        if AllNumbersUsed and re.match("^[0-9]+$", UserInput):
            for Count in range(0, len(Targets)):
                if Targets[Count] == int(UserInput):
                    Score += 2
                    Targets[Count] = -1
            AllNumbersUsed = False

        elif CheckIfUserInputValid(UserInput):
            UserInputInRPN = ConvertToRPN(UserInput)
            # Returns if  numbers used are allowed, and if all numbers were used
            UsedNumbersAllowed, AllNumbersUsed = CheckNumbersUsedAreAllInNumbersAllowed(NumbersAllowed, UserInputInRPN, MaxNumber)
            if UsedNumbersAllowed:
                IsTarget, Score = CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score)
                if IsTarget:
                    NumbersAllowed = RemoveNumbersUsed(UserInput, MaxNumber, NumbersAllowed)
                    NumbersAllowed = FillNumbers(NumbersAllowed, TrainingGame, MaxNumber)
                else:
                    # Even if used all numbers, if the final evaluated number is not in targets, cannot enter destroy-any-target mode
                    AllNumbersUsed = False
        Score -= 1
        if Targets[0] != -1:
            GameOver = True
        else:
            Targets = UpdateTargets(Targets, TrainingGame, MaxTarget)
    print("Game over!")
    DisplayScore(Score)

def CheckNumbersUsedAreAllInNumbersAllowed(NumbersAllowed, UserInputInRPN, MaxNumber):
    Temp = []
    for Item in NumbersAllowed:
        Temp.append(Item)
    for Item in UserInputInRPN:
        if CheckValidNumber(Item, MaxNumber):
            if int(Item) in Temp:
                Temp.remove(int(Item))
            else:
                return False, False
    # Second value checks if all numbers have been used
    return True, len(Temp) == 0

# # #