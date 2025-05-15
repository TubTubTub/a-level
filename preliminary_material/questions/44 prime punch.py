# # #

# Prime time punch. If the completed target was a prime number, destroy the targets on either side of the prime number (count them as scored)

def IsPrime(Target):
    # Iterate all integers from 2 up to target number (square rooted as at least one factor under root if not prime), if divisible then not a prime
    for Int in range(2, int(Target ** 0.5) + 1):
        if Target % Int == 0:
            return False

    return True

def CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score):
    UserInputEvaluation = EvaluateRPN(UserInputInRPN)
    UserInputEvaluationIsATarget = False
    if UserInputEvaluation != -1:
        for Count in range(0, len(Targets)):
            if Targets[Count] == UserInputEvaluation:
                Score += 2
                UserInputEvaluationIsATarget = True

                if IsPrime(Targets[Count]):
                    # If next number is not out of range nor is -1
                    if Count + 1 < len(Targets) and Targets[Count + 1] != -1:
                        Score += 2
                        Targets[Count + 1] = -1
                    # If previous number is not out of range nor is -1
                    if Count - 1 >= 0 and Targets[Count - 1] != -1:
                        Score += 2
                        Targets[Count - 1] = -1
                # Set current number after checking for prime, as needed in the if loop
                Targets[Count] = -1

    return UserInputEvaluationIsATarget, Score

# # #