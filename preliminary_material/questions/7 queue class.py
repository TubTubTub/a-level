# # #

# Code a Queue class instead of using a list

# Have to replace all Targets[Index] with Targets.get_at(Index)

class Queue:
    def __init__(self, Targets):
        self.Targets = Targets
    
    def __str__(self):
        res = ''
        for T in self.Targets:
            if T == -1:
                res += " "
            else:
                res += str(T)
            res += "|"
        return res

    def __len__(self):
        return len(self.Targets)
    
    def get_at(self, Index):
        return self.Targets[Index]
    
    def update(self, Index, New):
        self.Targets[Index] = New
    
    def enqueue(self, Target):
        self.Targets.append(Target)
    
    def dequeue(self):
        self.Targets.pop()
    
    def shift(self):
        # Alternatively just do Targets.pop(0)
        for Count in range (0, len(self.Targets) - 1):
            self.Targets[Count] = self.Targets[Count + 1]
        self.Targets.pop()

def Main():
    NumbersAllowed = []
    Targets = Queue([])
    MaxNumberOfTargets = 20
    MaxTarget = 0
    MaxNumber = 0
    TrainingGame = False
    Choice = input("Enter y to play the training game, anything else to play a random game: ").lower()
    print()
    if Choice == "y":
        MaxNumber = 1000
        MaxTarget = 1000
        TrainingGame = True
        Targets = Queue([-1, -1, -1, -1, -1, 4, 9, 140, 82, 121, 34, 45, 68, 75, 34, 23, 119, 43, 23, 119])
    else:
        MaxNumber = 10
        MaxTarget = 50
        Targets = CreateTargets(MaxNumberOfTargets, MaxTarget)
    NumbersAllowed = FillNumbers(NumbersAllowed, TrainingGame, MaxNumber)
    PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber)
    input()

def UpdateTargets(Targets, TrainingGame, MaxTarget):
    Targets.shift()
    if TrainingGame:
        Targets.enqueue(Targets.get_at(-1))
    else:
        Targets.enqueue(GetTarget(MaxTarget))
    return Targets

def CreateTargets(SizeOfTargets, MaxTarget):
    Targets = Queue([])
    for Count in range(1, 6):
        Targets.enqueue(-1)
    for Count in range(1, SizeOfTargets - 4):
        Targets.enqueue(GetTarget(MaxTarget))
    return Targets

# # #