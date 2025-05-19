# # #

# If a player uses very large numbers, i.e. numbers that lie beyond the defined MaxNumber that aren't allowed in NumbersAllowed, the program does not recognise this and will still reward a hit target. Make changes to penalise the player for doing so.

def CheckNumbersUsedAreAllInNumbersAllowed(NumbersAllowed, UserInputInRPN, MaxNumber):
    Temp = []
    for Item in NumbersAllowed:
        Temp.append(Item)
    for Item in UserInputInRPN:
        # If number not valid or not in NumbersAllowed, return false
        if CheckValidNumber(Item, MaxNumber) and int(Item) in Temp:
            Temp.remove(int(Item))
        else:
            return False
    return True

# # #