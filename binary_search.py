# - Running the program returns the following numbers in a list: [1, 2, 4, 7, 11, 22, 38, 42, 43]
# - Running the program returns an index of searched values in a list.
# - If there are no values, -1 is returned. (i.e. if the value is 4, 2 is returned)

# lista, amiben keresünk
array = [1, 2, 4, 7, 11, 22, 38, 42, 43]


# a függvényünknek megadunk 4 paramétert: a tömb, amiben keresünk, a keresett érték, az első index és az utolsó index
def my_search(array_for_search, value, min_index, max_index):
    # ha az utolsó indexből kivonjuk az elsőt és ez egyenlő eggyel...
    if max_index - min_index == 1:
        # és ha az első index egyenlő a keresett értékkel...
        if array_for_search[min_index] == value:
            # visszatérünk az első indexxel
            return min_index
        else:
            # máskülönben minusz eggyel térünk vissza
            return -1
    # a középső index egyenlő az utolsó index osztva kettővel
    mid = int((max_index - min_index) / 2)
    # ha a tömb középső indexe nagyobb mint a keresett érték...
    if array_for_search[min_index + mid] > value:
        # visszatérünk a my_serach() függvény meghívásával, amiben az utolsó index,
        # az utolsó indexből kivont középső index lesz
        return my_search(array_for_search, value, min_index, max_index - mid)
    else:
        # máskülönben a my_serach() függvény úgy hívjuk meg, hogy az első index,
        # az első indexhez hozzáadott középső index lesz és ezzel térünk vissza
        return my_search(array_for_search, value, min_index + mid, max_index)


# a függvényünknek megadunk 2 paramétert: a tömb, amiben keresünk és a keresett érték
def my_binary_search(array_for_search, value):
    # az érték a bekért inputtal egyenlő
    value = int(input("Enter a value: "))
    # visszatérünk a my_serach() függvény meghívásával, aminek átadjuk a tömböt,
    # a keresett értéket, a nullát mint első indexet, és a tömb hosszát, mint utolsó indexet
    return my_search(array_for_search, value, 0, len(array_for_search))


# kiíratjuk a keresett indexet egy kis kísérőszöveggel
print("Index of searched value: " + str(my_binary_search(array, 'index')))
