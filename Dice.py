# The game is played with five dice.
# The player is asked, "Roll dice?" at the beginning of each turn.
# If the player answers "n" or no, the game is over.
# If the player answers "y" or yes, the points are added to their score.
# The player scores 100 points for each one that is rolled.
# The player scores 50 points for each five that is rolled.
# The dice values and player score are displayed on the screen.
# If the player does not roll any ones or fives the game is over.
# The program must include a README file.
# The program must include class and method comments.
# The program must have at least two classes.
# The program must remain true to game play described in the overview.

import random
class number_of_dice:
    x = 5
class max_sided_di:
    x = 6


def main():
    score = 0
    roll = input('Roll dice? [y/n] ')
    while roll == "y": 
        roll_dice()
        get_score(score)
        if score == 0:
            roll = "n"
        roll = input('Roll dice? [y/n] ')
    

dice_number = 0

dice_rolls = []
def roll_dice():   
    total = number_of_dice()
    number_six = max_sided_di()
    dice_rolls.clear()
    for x in range(total.x):
        dice_number = random.randint(1,number_six.x)
        dice_rolls.append(dice_number)
    return print(dice_rolls)


def get_score(score):
    for x in dice_rolls:
        if x == 5:
            score += 50
        elif x == 1:
            score += 100
    y = dice_rolls.count(5)
    z = dice_rolls.count(1)
    if y == 0 and z == 0:
        score = 0
    return print(score)

if __name__ == "__main__":
    main()