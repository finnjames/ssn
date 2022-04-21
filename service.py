import os

import tools


class User:
    def __init__(self, name: str):
        self.name = name
        self.uid = self.generate_uid()
        self.Y = None
        self.A = None
        self.c = None

    def generate_uid(self):
        return tools.get_random_int()

    def to_tuple(self):
        return (self.name, self.uid, self.Y, self.A, self.c)


class Service:
    def __init__(self, name="Service"):
        self.name = name
        self.users = {}

    def new_user(self, name: str):
        new_user = User(name)
        self.users[new_user.uid] = new_user
        return new_user.uid

    def get_challenge(self, uid, Y, A, q):
        self.users[uid].Y = Y
        self.users[uid].A = A
        c = tools.get_random_int(q)
        self.users[uid].c = c
        return c

    def verify(self, uid, g, p, z):
        _, _, Y, A, c = self.users[uid].to_tuple()

        print(f"{Y=}\n{A=}\n{c=}\n{g=}\n{p=}\n{z=}\n")

        return A * pow(Y, c, p) % p == pow(g, z, p)
