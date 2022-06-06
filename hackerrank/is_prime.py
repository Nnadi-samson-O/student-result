def is_prime(a):
    if not isinstance(a, int):
        print(False)
    if a < 2:
        print(False)

    first_five_prime = [2, 3, 5, 7, 11]
    if a in first_five_prime:
        print(True)

    if a > 11:
        for i in first_five_prime:
            if a % i == 0:
                print(False)
            return True
is_prime(76)