import random


def get_random_int(q=pow(2, 128)):
    return random.SystemRandom().randint(0, q)  # TODO: how to use 2048 bits?


def get_random_power(g, q):
    return pow(g, random.SystemRandom().randint(0, q))
