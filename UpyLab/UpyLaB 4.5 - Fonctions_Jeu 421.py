import random


def alea_dice(s):
    random.seed(s)
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    if dice1 in (4, 2, 1) and dice2 in (4, 2, 1) and dice3 in (4, 2, 1):
        # ou if dice1 + dice2 + dice3 == 7
        return True
    else:
        return False


print(alea_dice(25))
