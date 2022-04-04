import random


def get_random_int():
    return random.SystemRandom().randint(0, 2**16)  # TODO: how to use 2048 bits?
