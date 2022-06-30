# Sieve of Eratosthenes algorithm
def my_is_prime(n):

    if n < 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def my_print_prime(n):

    if n > 0:
        for i in range(2, n + 1):
            if my_is_prime(i):
                print(i, end=" ")


if __name__ == "__main__":
    n = int(input('Enter a number: '))

    if n >= 2:
        print('All prime numbers, that are lesser or equal to your choice: ')
    else:
        print('There are no lesser or equal primes to your choice.')

    my_print_prime(n)
