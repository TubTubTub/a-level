# # #

# Allowed numbers don’t have any duplicate numbers, and can be used multiple times

def RemoveNumbersUsed(UserInput, MaxNumber, NumbersAllowed):
    # Initialiate list of unique numbers in UserInput
    SeenNumbers = []
    UserInputInRPN = ConvertToRPN(UserInput)
    for Item in UserInputInRPN:
        if CheckValidNumber(Item, MaxNumber):
            Item = int(Item)
            # Only remove a number once from NumbersAllowed regardless of how many times used, the first time its seen in UserInput
            if Item in NumbersAllowed and Item not in SeenNumbers:
                SeenNumbers.append(Item)
                NumbersAllowed.remove(Item)
    return NumbersAllowed

def CheckNumbersUsedAreAllInNumbersAllowed(NumbersAllowed, UserInputInRPN, MaxNumber):
    Temp = []
    for Item in NumbersAllowed:
        Temp.append(Item)
    for Item in UserInputInRPN:
        # Valid even if number used more times than allowed in NumbersAllowed
        if CheckValidNumber(Item, MaxNumber) and int(Item) not in Temp:
            return False
    return True

# # #