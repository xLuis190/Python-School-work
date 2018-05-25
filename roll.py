from random import *
def roll(selection):
    dice = [2,2,1,3,5]
    for s in selection:
        dice[s -1] = randint(1,6)
    print(dice)
