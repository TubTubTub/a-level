1. Support brackets using the shunting yard algorithm. Perhaps there is a nice recursive solution using the existing ConvertToRPN function.
2. Support another operator, e.g. ^. This seems likely since 2^3 = 8 and (3+8)^2 = 121 (in the training game) -- but hang on, the ^ operator is right-associative.... Perhaps implement the modulo (%) or integer division (//, but this is two characters so maybe |) operator instead, since these are left-associative.
3. Support a single-integer answer
4. Ignore spaces in the input
5. Different way of dealing with invalid input (instead of deducting marks) or implement some other way of enhancing input validation, such as detecting divide by zero errors, perhaps by handling ZeroDivisionError.
6. Save game / high score, etc
7. Code a Queue class instead of using a list
8. Check that the result is an int instead of just converting it to int
9. Score one rather than all of the repeated targets (e.g. 23 in the training game)
10. Something to do with the difference between MaxTarget and MaxNumber in the normal game and training game
11. Regenerate the list of available numbers, perhaps at the cost of 1 point
12. Display a summary of the targets that were achieved, and how, at the end of the game.
13. Implement a "streak" bonus.
14. Implement "easy" and "hard" modes, in which the target range is adjusted.
15. Allow the user to choose the NumbersAllowed. They would have to be fixed for that game I think.
16. Adjust the score based on efficiency, by awarding more for using fewer operators.
17. For a small points cost, regenerate the NumbersAllowed or eliminate a particular target number.
18. Add support for negative numbers.
19. Implement a mode in which the potential operators are limited, for instance + and - only.
20. Support floating point numbers during calculation. At the moment, every result of a calculation is rounded down.
21. Calculate and display game statistics.
22. Add an option to restart or quit the game.

# Following from wiki (https://en.wikibooks.org/wiki/A-level_Computing/AQA/Paper_1/Skeleton_program/2025)

23. Fix the scoring bug whereby n targets cleared give you 2n-1 points instead of n points
24. Modify the program so that (1) the player can use each number more than once and (2) the game does not allow repeats within the 5 numbers given
25. Modify the program to accept input in Postfix (Reverse Polish Notation) instead of Infix
26. Allow the program to not stop after 'Game Over!' with no way for the user to exit.
27. Add the ability to clear any target
28. Allowed numbers don’t have any duplicate numbers, and can be used multiple times
29. Once a target is cleared, prevent it from being generated again
30. If a player uses very large numbers, i.e. numbers that lie beyond the defined MaxNumber that aren't allowed in NumbersAllowed, the program does not recognise this and will still reward a hit target. Make changes to penalise the player for doing so.
31. Fix the bug where two digit numbers in random games can be entered as sums of numbers that don't occur in the allowed numbers list. Ie the target is 48, you can enter 48-0 and it is accepted.
32. Implement a feature where every round, a random target (and all its occurences) is shielded, and cannot be targeted for the duration of the round. If targeted, the player loses a point as usual. The target(s) should be displayed surrounded with brackets like this: |(n)|
33. Do not advance the target list forward for invalid entries, instead inform the user the entry was invalid and prompt them for a new one
34. Implement a menu where the user can start a new game or quit their current game
35. Increase the score with a bonus equal to the quantity of allowable numbers used in a qualifying expression
36. Implement a multiplicative score bonus for each priority (first number in the target list) number completed sequentially
37. If the user creates a qualifying expression which uses all the allowable numbers, grant the user a special reward ability (one use until unlocked again) to allow the user to enter any number of choice and this value will be removed from the target list
38. When a target is cleared, put a £ symbol in its position in the target list. When the £ symbol reaches the end of the tracker, increase the score by 1
39. Implement a victory condition which allows the player to win the game by achieving a certain score. Allow the user to pick difficulty, e.g. easy (10), normal (20), hard (40)
40. Shotgun. If an expression exactly evaluates to a target, the score is increased by 3 and remove the target as normal. If an evaluation is within 1 of the target, the score is increased by 1 and remove those targets too
41. Every time the user inputs an expression, shuffle the current position of all targets (cannot push a number closer to the end though)
42. Speed Demon. Implement a mode where the target list moves a number of places equal to the current player score. Instead of ending the game when a target gets to the end of the tracker, subtract 1 from their score. If their score ever goes negative, the player loses
43. Multiple of X. The program should randomly generate a number each turn, e.g. 3 and if the user creates an expression which removes a target which is a multiple of that number, give them a bonus of their score equal to the multiple (in this case, 3 extra score)
44. Prime time punch. If the completed target was a prime number, destroy the targets on either side of the prime number (count them as scored)
45. Allow the user to specify the highest number within the five NumbersAllowed