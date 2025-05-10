# # #

# Implement a feature where every round, a random target (and all its occurences) is shielded, and cannot be targeted for the duration of the round. If targeted, the player loses a point as usual. The target(s) should be displayed surrounded with brackets like this: |(n)|

import random

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber):
    Score = 0
    GameOver = False
    while not GameOver:
        # Choose random number as protected target
        ProtectedTarget = -1
        while ProtectedTarget == -1:
            ProtectedTarget = random.choice(Targets)

        # Pass ProtectedTarget
        DisplayState(Targets, NumbersAllowed, Score, ProtectedTarget)
        UserInput = input("Enter an expression: ")
        print()
        if CheckIfUserInputValid(UserInput):
            UserInputInRPN = ConvertToRPN(UserInput)
            if CheckNumbersUsedAreAllInNumbersAllowed(NumbersAllowed, UserInputInRPN, MaxNumber):
                # Pass ProtectedTarget
                IsTarget, Score = CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score, ProtectedTarget)
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

# Receive ProtectedNumber
def CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score, ProtectedTarget):
    UserInputEvaluation = EvaluateRPN(UserInputInRPN)
    UserInputEvaluationIsATarget = False
    if UserInputEvaluation != -1:
        for Count in range(0, len(Targets)):
            if Targets[Count] == UserInputEvaluation:
                # Check if target is ProtectedTarget
                if Targets[Count] != ProtectedTarget:
                    Score += 2
                    Targets[Count] = -1
                    UserInputEvaluationIsATarget = True
                else:
                    print('Evaluated to protected target!')
                    print()
    return UserInputEvaluationIsATarget, Score

# Receive ProtectedTarget
def DisplayState(Targets, NumbersAllowed, Score, ProtectedTarget):
    # Pass ProtectedTarget
    DisplayTargets(Targets, ProtectedTarget)
    DisplayNumbersAllowed(NumbersAllowed)
    DisplayScore(Score)

# Receive ProtectedTarget
def DisplayTargets(Targets, ProtectedTarget):
    print("|", end = '')
    for T in Targets:
        if T == -1:
            print(" ", end = '')
        # Display ProtectedTarget
        elif T == ProtectedTarget:
            print(f"~~ {T} ~~", end='')
        else:
            print(T, end = '')
        print("|", end = '')
    print()
    print()

# # #