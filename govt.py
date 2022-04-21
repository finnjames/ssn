import tools
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

import os


class Citizen:
    def __init__(self, name: str, q: int):
        self.name = name
        self.ssn = tools.get_random_int(q)


class Govt:
    def __init__(self):
        self.citizens = {}

    def register(self, name: str, q: int):
        new_citizen = Citizen(name, q)
        self.citizens[name] = new_citizen
        return new_citizen.ssn

    def generate_key(ssn: bytes):
        salt = os.urandom(16)
        kdf = Scrypt(salt=salt, length=32, n=pow(2, 14), r=8, p=1)
        return kdf.derive(ssn)
