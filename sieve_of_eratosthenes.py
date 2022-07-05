# - [OPTIONAL] Running the program returns a list of all prime numbers, that are lesser or equal to the parameter N.

# függvény, ami kiszűri a prím számokat, a paraméterben átadott számig
def is_prime(n):
    # ha a paraméterben átadott szám kisebb, mint 1...
    if n < 1:
        # akkor az érték nem prím szám
        return False
    # egy for ciklus segítségével 2-től indulva végigiterálunk a számokon egészen a paraméterben átadott számig
    for i in range(2, n):
        # ha a paraméterben átadott szám maradéktalanul megvan az iterációban éppen sorrakerülő értében...
        if n % i == 0:
            # akkor az érték nem prím szám
            return False
    # máskülönben az érték prím szám
    return True


# függvény, ami kiírja az inputként átadott számig, az összes prím számot
def my_print_prime():
    # az n változó az iputban átadott értékkel egyenlő
    n = int(input('Enter a number: '))
    # ha az inputban átadott szám nagyobb vagy egyenlő, mint 2
    if n >= 2:
        # kiírunk egy üzenetet a kívánt számok elé
        print('All prime numbers, that are lesser or equal to your choice: ')
    else:
        # kiírunk egy üzenetet, ami jelzi, hogy a tartományban nincsenek prím számok
        print('There are no lesser or equal primes to your choice.')
    # ha a paraméterben átadott szám nagyobb, mint nulla
    if n > 0:
        # egy for ciklus segítségével végigiterálunk 2-től egészen a paraméterben megadott szám + 1-ig
        for i in range(2, n + 1):
            # minden iterációban ellenőrizzük, hogy segédváltozó értéke prím szám-e
            if is_prime(i):
                # ha pedig igen kiíratjuk, egy szóközzel utána, majd a következőt is ugyanígy
                print(i, end=" ")


# meghívjuk a függvényt
my_print_prime()
