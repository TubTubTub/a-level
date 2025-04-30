# # #

# Support floating point numbers during calculation. At the moment, every result of a calculation is rounded down.

import re
import random
import math

def CheckNumbersUsedAreAllInNumbersAllowed(NumbersAllowed, UserInputInRPN, MaxNumber):
    Temp = []
    for Item in NumbersAllowed:
        Temp.append(Item)
    for Item in UserInputInRPN:
        if CheckValidNumber(Item, MaxNumber):
            # Float each item so that they are atually checked, instead of int() rounded versions
            if float(Item) in Temp:
                Temp.remove(float(Item))
            else:
                return False
    return True

def CheckValidNumber(Item, MaxNumber):
    # Add check for decimal part
    if re.search("^[0-9]+([.][0-9]+)?$", Item) is not None:
        ItemAsInteger = float(Item)
        if ItemAsInteger > 0 and ItemAsInteger <= MaxNumber:
            return True
    return False

def EvaluateRPN(UserInputInRPN):
    S = []
    while len(UserInputInRPN) > 0:
        while UserInputInRPN[0] not in ["+", "-", "*", "/"]:
            S.append(UserInputInRPN[0])
            UserInputInRPN.pop(0)
        Num2 = float(S[-1])
        S.pop()
        Num1 = float(S[-1])
        S.pop()
        Result = 0.0
        if UserInputInRPN[0] == "+":
            Result = Num1 + Num2
        elif UserInputInRPN[0] == "-":
            Result = Num1 - Num2
        elif UserInputInRPN[0] == "*":
            Result = Num1 * Num2
        elif UserInputInRPN[0] == "/":
            Result = Num1 / Num2
        UserInputInRPN.pop(0)
        S.append(str(Result))
    
    # Floor number no matter what
    return math.floor(float(S[0]))

def GetNumberFromUserInput(UserInput, Position):
    Number = ""
    MoreDigits = True
    while MoreDigits:
        # Also check for . when checking for string of number
        if not(re.search("[0-9]|[.]", str(UserInput[Position])) is None):
            Number += UserInput[Position]
        else:
            MoreDigits = False
        Position += 1
        if Position == len(UserInput):
            MoreDigits = False
    if Number == "":
        return -1, Position
    else:
        return float(Number), Position

def CheckIfUserInputValid(UserInput):
    # Add check for decimal part
    if re.search("^([0-9]+([.][0-9]+)?[\\+\\-\\*\\/])+[0-9]+([.][0-9]+)?$", UserInput) is not None:
        return True
    else:
        return False

def GetNumber(MaxNumber):
    # Generate allowed numbers that include floating points
    return round(random.uniform(1, MaxNumber), 2)

# # #