import random

# Used to determine the amount of dice needed for the game. 
class number_of_dice:
    x = 5
# Used to determine the max number a di can roll.
class max_sided_di:
    x = 6

# Main() asks the user if they want to roll dice, and if they want to continue rolling dice.
def main():
    score = 0
    roll = input('Roll dice? [y/n] ')
    while roll == "y" or roll == "Y": 
        roll_dice()
        get_score(score)
        if score == 0:
            roll = "n"
        roll = input('Roll dice? [y/n] ')
    

dice_number = 0
dice_rolls = []

# Gets the values of the five dice rolled and stores them into the empty array dice_rolls. The array is emptied each time the function is used.
def roll_dice():   
    total = number_of_dice()
    number_six = max_sided_di()
    dice_rolls.clear()
    for x in range(total.x):
        dice_number = random.randint(1,number_six.x)
        dice_rolls.append(dice_number)
    return print(dice_rolls)

# Gets the score of the dice by iterating through the dice_rolls array. y and z are variables to verify at least a five or a one was rolled.
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