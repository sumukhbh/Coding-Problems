# Given a dice which rolls from 1 to 7(with uniform probability) simulate a 5 sided die #

import random
def roll_dice():
    return random.randint(1,7)

def dice_simulator():
    roll_val = 7

    while roll_val > 5:
        roll_val = roll_dice()

    print("You rolled a :", roll_val)

dice_simulator()
    
