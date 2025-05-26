# # #

# Every time the user inputs an expression, shuffle the current position of all targets (cannot push a number closer to the end though)

import random

def UpdateTargets(Targets, TrainingGame, MaxTarget):
    for Count in range (0, len(Targets) - 1):
        Targets[Count] = Targets[Count + 1]
    Targets.pop()

    # Get a list of indices, for every slot in the list that contains a target
    NumberIndices = [Index for Index, Item in enumerate(Targets) if Item != -1]
    for Index, Number in enumerate(Targets):
        if Number == -1:
            # Don't swap positions with empty slots
            continue
        else:
            IndexToSwap = random.choice(NumberIndices)
            # Choose a random index, and swap the current target with the target at that index
            Targets[Index], Targets[IndexToSwap] = Targets[IndexToSwap], Targets[Index]

    if TrainingGame:
        Targets.append(Targets[-1])
    else:
        Targets.append(GetTarget(MaxTarget))
    return Targets

# # #