# # #

# Support brackets using the shunting yard algorithm. Perhaps there is a nice recursive solution using the existing ConvertToRPN function.

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber):
    Score = 0
    GameOver = False
    while not GameOver:
        DisplayState(Targets, NumbersAllowed, Score)
        UserInput = input("Enter an expression: ")
        print()

        # Removed CheckIfUserInputValid, added to RPNWithBrackets function
        UserInputEvaluation, Valid = RPNWithBrackets(UserInput)
        UserInputWithoutBrackets = UserInput.replace("(", "").replace(")", "")
        TokensWithoutBrackets = ConvertToRPN(UserInputWithoutBrackets)

        # If UserInput is valid, from RPNWithBrackets function
        # Pass UserInput tokens without brackets
        if Valid and CheckNumbersUsedAreAllInNumbersAllowed(NumbersAllowed, TokensWithoutBrackets, MaxNumber):
            # Pass in evaluated number instead of UserInputInRPN
            IsTarget, Score = CheckIfUserInputEvaluationIsATarget(Targets, Score, UserInputEvaluation)
            if IsTarget:
                NumbersAllowed = RemoveNumbersUsed(UserInputWithoutBrackets, MaxNumber, NumbersAllowed)
                NumbersAllowed = FillNumbers(NumbersAllowed, TrainingGame, MaxNumber)

        Score -= 1
        if Targets[0] != -1:
            GameOver = True
        else:
            Targets = UpdateTargets(Targets, TrainingGame, MaxTarget)
    print("Game over!")
    DisplayScore(Score)

# Receive already calculated UserInputEvaluation
def CheckIfUserInputEvaluationIsATarget(Targets, Score, UserInputEvaluation):
    UserInputEvaluationIsATarget = False
    if UserInputEvaluation != -1:
        for Count in range(0, len(Targets)):
            if Targets[Count] == UserInputEvaluation:
                Score += 2
                Targets[Count] = -1
                UserInputEvaluationIsATarget = True
    return UserInputEvaluationIsATarget, Score

# Gets the - first or most outer scoped - expression in brackets, and returns the expression and indices of the opening and closing brackets
def GetSubstring(String):
    First = -1
    Stack = 0

    for Index, Char in enumerate(String):
        if Char == "(" and First == -1:
            First = Index

        if Char == "(":
            Stack += 1

        elif Char == ")":
            Stack -= 1

            if Stack == 0:
                return String[First + 1 : Index], First, Index

# While UserInput contains brackets, get all expressions within the brackets and replace it with its evaluated output
# Also checks if each expression within brackets is valid, and when the final processed UserInput without brackets is valid
def RPNWithBrackets(UserInput):
    while "(" in UserInput and ")" in UserInput:
        Substring, First, Last = GetSubstring(UserInput)
        Evaluated, Valid = RPNWithBrackets(Substring)

        if Valid is False:
            return -1, False
        else:
            UserInput = UserInput[:First] + str(Evaluated) + UserInput[Last + 1:]

    if not(CheckIfUserInputValid(UserInput)):
        return -1, False

    # Convert the bracketless UserInput into RPN, and then calculate the output
    StringRPN = ConvertToRPN(UserInput)
    Evaluated = EvaluateRPN(StringRPN)

    return Evaluated, True

# # #