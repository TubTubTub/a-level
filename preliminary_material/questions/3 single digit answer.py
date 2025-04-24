# # #

# Support a single-integer answer

import re
import math

def CheckIfUserInputValid(UserInput):
    # Changed first group from + to *
    if re.search("^([0-9]+[\\+\\-\\*\\/\\^])*[0-9]+$", UserInput) is not None:
        return True
    else:
        return False

def EvaluateRPN(UserInputInRPN):
    if len(UserInputInRPN) == 1:
        S = UserInputInRPN
    else:
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

    if float(S[0]) - math.floor(float(S[0])) == 0.0:
        return math.floor(float(S[0]))
    else:
        return -1
# # #