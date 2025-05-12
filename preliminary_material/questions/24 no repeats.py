# # #

# Modify the program so that (1) the player can use each number more than once and (2) the game does not allow repeats within the 5 numbers given

def FillNumbers(NumbersAllowed, TrainingGame, MaxNumber):
    if TrainingGame:
        return [2, 3, 2, 8, 512]
    else:
        # Restart loop in attempting to append number that is already in NumbersAllowed
        while len(NumbersAllowed) < 5:
            Number = GetNumber(MaxNumber)
            if Number not in NumbersAllowed:
                NumbersAllowed.append(Number)

        return NumbersAllowed

# # #