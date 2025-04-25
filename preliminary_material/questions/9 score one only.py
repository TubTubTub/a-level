# # # 

# Score one rather than all of the repeated targets (e.g. 23 in the training game)

def CheckIfUserInputEvaluationIsATarget(Targets, UserInputInRPN, Score):
    UserInputEvaluation = EvaluateRPN(UserInputInRPN)
    UserInputEvaluationIsATarget = False
    if UserInputEvaluation != -1:
        for Count in range(0, len(Targets)):
            if Targets[Count] == UserInputEvaluation:
                Score += 2
                Targets[Count] = -1
                UserInputEvaluationIsATarget = True
                # Add break to stop loop when first correct answer found
                break
    return UserInputEvaluationIsATarget, Score

# # #