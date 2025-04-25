# # #

# Save game / high score, etc

class Game:
    def __init__(self, Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber, Score):    
        self.Targets = Targets
        self.NumbersAllowed = NumbersAllowed
        self.TrainingGame = TrainingGame
        self.MaxTarget = MaxTarget
        self.MaxNumber = MaxNumber
        self.Score = Score

    def save(self):
        with open('save.txt', 'w') as f:
            f.write(','.join([str(num) for num in self.Targets]) + '\n')
            f.write(','.join([str(num) for num in self.NumbersAllowed]) + '\n')
            f.write(('1' if self.TrainingGame else '0') + '\n')
            f.write(str(self.MaxTarget) + '\n')
            f.write(str(self.MaxNumber) + '\n')
            f.write(str(self.Score) + '\n')
    
    @classmethod
    def load_game(cls):
        try:
            with open('save.txt', 'r') as f:
                line = f.readline().strip()
                Targets = [int(x) for x in line.split(',')]
                line = f.readline().strip()
                NumbersAllowed = [int(x) for x in line.split(',')]
                line = f.readline().strip()
                TrainingGame = True if line == '1' else False
                line = f.readline().strip()
                MaxTarget = int(line)
                line = f.readline().strip()
                MaxNumber = int(line)
                line = f.readline().strip()
                Score = int(line)
            
            return cls(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber, Score)

        except FileNotFoundError:
            return False
        
def Main():
    NumbersAllowed = []
    Targets = []
    MaxNumberOfTargets = 20
    MaxTarget = 0
    MaxNumber = 0
    TrainingGame = False
    Choice = input("Enter y to play the training game, l to load game, anything else to play a random game: ").lower()
    print()
    if Choice == "y":
        MaxNumber = 1000
        MaxTarget = 1000
        TrainingGame = True
        Targets = [-1, -1, -1, -1, -1, 23, 9, 140, 82, 121, 34, 45, 68, 75, 34, 23, 119, 43, 23, 119]
        NumbersAllowed = FillNumbers(NumbersAllowed, TrainingGame, MaxNumber)
        Score = 0
    elif Choice.lower() == "l":
        SavedGame = Game.load_game()

        if SavedGame is False:
            print('No saved game found! Starting random game...')
            print()
            MaxNumber = 10
            MaxTarget = 50
            Targets = CreateTargets(MaxNumberOfTargets, MaxTarget)
            NumbersAllowed = FillNumbers(NumbersAllowed, TrainingGame, MaxNumber)
            Score = 0
        else:
            MaxNumber = SavedGame.MaxNumber
            MaxTarget = SavedGame.MaxTarget
            TrainingGame = SavedGame.TrainingGame
            Targets = SavedGame.Targets
            NumbersAllowed = SavedGame.NumbersAllowed
            Score = SavedGame.Score
    else:
        MaxNumber = 10
        MaxTarget = 50
        Targets = CreateTargets(MaxNumberOfTargets, MaxTarget)
        NumbersAllowed = FillNumbers(NumbersAllowed, TrainingGame, MaxNumber)
        Score = 0

    PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber, Score)
    input()

def PlayGame(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber, Score):
    GameOver = False
    while not GameOver:
        DisplayState(Targets, NumbersAllowed, Score)
        UserInput = input("Enter an expression: ")
        print()

        if UserInput.upper() == 'S':
            SavedGame = Game(Targets, NumbersAllowed, TrainingGame, MaxTarget, MaxNumber, Score)
            SavedGame.save()
            print('Game saved!')
            print()
            continue

        if CheckIfUserInputValid(UserInput):
            UserInputInRPN = ConvertToRPN(UserInput)
            if CheckNumbersUsedAreAllInNumbersAllowed(NumbersAllowed, UserInputInRPN, MaxNumber):
                IsTarget, Score = CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score)
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