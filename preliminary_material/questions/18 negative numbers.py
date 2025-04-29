# # #

# Add support for negative numbers.

# Only have to change GetNumberFromUserInput

import re

def GetNumberFromUserInput(UserInput, Position):
    # Search string for number, and optional - before that
    Search = re.search("-?[0-9]+", str(UserInput[Position:]))
    if Search is not None:
        # Get indices of match, but have to add starting position to indices to get the index in the actual full UserINnput
        Indicies = [Index + Position for Index in Search.span()]
        Number = UserInput[Indicies[0]:Indicies[1]]
        # Return normal Position, but max length of string if reaching end of the string
        return int(Number), min(Indicies[1] + 1, len(UserInput))
    else:
       return -1, Position + 1

# Allow negative targets
def GetTarget(MaxTarget):
    return random.randint(-MaxTarget, MaxTarget)

# Allow negative allowed numbers
def GetNumber(MaxNumber):
    return random.randint(-MaxNumber, MaxNumber)

# # #