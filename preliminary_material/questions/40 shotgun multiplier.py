# # #

# Shotgun. If an expression exactly evaluates to a target, the score is increased by 3 and remove the target as normal. If an evaluation is within 1 of the target, the score is increased by 1 and remove those targets too

def CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score):
    UserInputEvaluation = EvaluateRPN(UserInputInRPN)
    UserInputEvaluationIsATarget = False
    if UserInputEvaluation != -1:
        for Count in range(0, len(Targets)):
            if Targets[Count] == UserInputEvaluation:
                # Add score of 3
                Score += 4
                Targets[Count] = -1
                UserInputEvaluationIsATarget = True

            # Check if UserInputEvaluation is within one of target
            elif (Targets[Count] + 1) == UserInputEvaluation or (Targets[Count] - 1) == UserInputEvaluation:
                # Add score of 1
                Score += 2
                Targets[Count] = -1
                UserInputEvaluationIsATarget = True
    return UserInputEvaluationIsATarget, Score

# # #