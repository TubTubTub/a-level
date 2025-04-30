# # #

# Add an option to restart or quit the game.

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber):
    Score = 0
    GameOver = False
    while not GameOver:
        DisplayState(Targets, NumbersAllowed, Score)
        UserInput = input("Enter an expression: ")
        print()
        
        if UserInput == "r" or UserInput == "R":
            Confirm = input("Are you sure you want to restart (y/n): ")
            print()
            if Confirm.lower() == "y":
                # Rerun Main() if restarting the game
                Main()
                return
            else:
                # Restart loop if cancel
                continue
        # Use elif here instead of else
        elif UserInput == "q" or UserInput == "Q":
            Confirm = input("Are you sure you want to quit (y/n): ")
            print()
            if Confirm.lower() == "y":
                # Print game over stats
                print("Game over!")
                DisplayScore(Score)
                # Return to quit game
                return
            else:
                continue

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