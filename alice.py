import govt
import service
from cryptography.hazmat.primitives.asymmetric import dh
import tools


def print_as_hex(data: bytes):
    print(data.hex())


def main():

    NAME = "Alice"

    # TODO: This is just to get a large prime number
    params = dh.generate_parameters(generator=2, key_size=512)
    p = params.parameter_numbers().p

    g = pow(tools.get_random_int(p), 2, p)
    q = int((p + 1) / 2) - 1

    print(f"{pow(g, q - 1, p)==g}")

    print(f"g={g}, p={p}, q={q}")

    # generate SSN
    my_govt = govt.Govt()
    ssn = my_govt.register(NAME, q)

    my_service = service.Service()
    uid = my_service.new_user(NAME)

    r = tools.get_random_int(q)

    Y = pow(g, ssn, p)
    A = pow(g, r, p)

    c = my_service.get_challenge(uid, Y, A, q)

    z = r + (c * ssn) % p

    if my_service.verify(uid, g, p, z):
        print("Successfully verified!\n")
        return 0
    else:
        print("Failed to verify!\n")
        return 1

    # show credentials anonymously


if __name__ == "__main__":
    REPETITIONS = 100
    for i in range(REPETITIONS):
        if main() > 0:
            break
