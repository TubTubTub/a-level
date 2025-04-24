# # #

# Support brackets using the shunting yard algorithm. Perhaps there is a nice recursive solution using the existing ConvertToRPN function.

# Replaces ConvertToRPN and EvaluateRPN

# UserInput never has spaces in it due to CheckIfUserInputValid

import re

def GetNumberFromUserInput(UserInput, Position):
    Number = ""
    MoreDigits = True
    while MoreDigits:
        if not(re.search("[0-9]", str(UserInput[Position])) is None):
            Number += UserInput[Position]
        else:
            MoreDigits = False
        Position += 1
        if Position == len(UserInput):
            MoreDigits = False
    if Number == "":
        return -1, Position
    else:
        return int(Number), Position

def ApplyOperation(Operand1, Operand2, Operator):
    match Operator:
        case '+': return Operand1 + Operand2
        case '-': return Operand1 - Operand2
        case '*': return Operand1 * Operand2
        case '/': return Operand1 / Operand2

def ShuntingYard(UserInput):
    Precedence = {"(": 0, ")": 0, "+": 2, "-": 2, "*": 4, "/": 4}

    Position = 0
    Operators = []
    Operands = []

    while Position < len(UserInput):
        if UserInput[Position] == '(':
            Operators.append('(')
            Position += 1

        elif UserInput[Position].isdigit():
            Operand, NewPosition = GetNumberFromUserInput(UserInput, Position)
            Operands.append(Operand)

            if NewPosition == len(UserInput): # As GetNumberFromUserInput gives +1 Position instead of +2 Position if end of UserInput reached
                break
            else:
                Position = NewPosition - 1

        elif UserInput[Position] == ')':
            while len(Operators) > 0 and Operators[-1] != '(':
                Operand2 = Operands.pop()
                Operand1 = Operands.pop()
                Operator = Operators.pop()

                Operands.append(ApplyOperation(Operand1, Operand2, Operator))

            Operators.pop() # Remove opening bracket

            Position += 1

        else:
            while len(Operators) > 0 and Precedence[Operators[-1]] > Precedence[UserInput[Position]]:
                Operand2 = Operands.pop()
                Operand1 = Operands.pop()
                Operator = Operators.pop()

                Operands.append(ApplyOperation(Operand1, Operand2, Operator))

            Operators.append(UserInput[Position])

            Position += 1

    while len(Operators) > 0:
        Operand2 = Operands.pop()
        Operand1 = Operands.pop()
        Operator = Operators.pop()

        Operands.append(ApplyOperation(Operand1, Operand2, Operator))

    return Operands[-1]

Answer = ShuntingYard('(333+5)*9-53')

print(Answer)

# # #

# # #

# Alternative answer

import re

def GreaterPrecedence(Operator1, Operator2):
    Precedence = {"+": 2, "-": 2, "*": 4, "/": 4}
    return Precedence[Operator1] > Precedence[Operator2]

def ApplyOperator(OperatorStack, ValueQueue):
    Operator = OperatorStack.pop()
    RightValue = ValueQueue.pop()
    LeftValue = ValueQueue.pop()
    Result = eval(f'{LeftValue}{Operator}{RightValue}')
    ValueQueue.append(Result)

def PeekStack(Stack):
    if len(Stack) == 0:
        return None
    return Stack[-1]

def ShuntingYard(InfixExpression, MaxNumber):
    Tokens = re.findall("[+/*()-]|\d+", InfixExpression)
    ValueQueue = []
    OperatorStack = []

    for Token in Tokens:
        if Token.isnumeric():
            if (CheckValidNumber(Token, MaxNumber) is False):
                return -1
            ValueQueue.append(int(Token))

        elif Token == '(':
            OperatorStack.append(Token)

        elif Token == ')':
            while PeekStack(OperatorStack) and PeekStack(OperatorStack) != '(':
                ApplyOperator(OperatorStack, ValueQueue)
            OperatorStack.pop()

        else:
            while (PeekStack(OperatorStack)) and (PeekStack(OperatorStack) not in '()') and (GreaterPrecedence(PeekStack(OperatorStack), Token)):
                ApplyOperator(OperatorStack, ValueQueue)

            OperatorStack.append(Token)

    while PeekStack(OperatorStack):
        ApplyOperator(OperatorStack, ValueQueue)
    return ValueQueue[0]

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber):
    Score = 0
    GameOver = False
    while not GameOver:
        DisplayState(Targets, NumbersAllowed, Score)
        UserInput = input("Enter an expression: ")
        print()

        # if CheckIfUserInputValid(UserInput):
        #     UserInputInRPN = ConvertToRPN(UserInput)
        #     if CheckNumbersUsedAreAllInNumbersAllowed(NumbersAllowed, UserInputInRPN, MaxNumber):

        OutputValue = ShuntingYard(UserInput, MaxNumber)

        IsTarget, Score = CheckIfUserInputEvaluationIsATarget(Targets, OutputValue, Score)
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