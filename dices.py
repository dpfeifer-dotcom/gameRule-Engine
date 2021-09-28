import random


def roll_1D6():
    return random.randint(1, 6)


def roll_2d6():
    return roll_1D6() + roll_1D6()


def roll_3d6():
    return roll_2d6() + roll_1D6()
