import govt
import service
from cryptography.hazmat.primitives.asymmetric import dh
import tools


def print_as_hex(data: bytes):
    print(data.hex())


def main():

    NAME = "Alice"

    # generate SSN
    g = govt.Govt()
    ssn = g.register(NAME)

    s = service.Service()
    uid = s.new_user(NAME)

    # TODO: I feel like this is not how I should be doing this
    params = dh.generate_parameters(generator=2, key_size=512)
    g = params.parameter_numbers().g

    r = tools.get_random_int()

    Y = g**ssn % g
    A = g**r % g

    c = s.get_challenge(uid, Y, A)

    z = r + (c * ssn) % g

    if s.verify(uid, g, z):
        print("Successfully verified!")
        return 0
    else:
        print("Failed to verify!")
        return 1

    # show credentials anonymously


if __name__ == "__main__":
    REPETITIONS = 10
    for i in range(REPETITIONS):
        if main() > 0:
            break
