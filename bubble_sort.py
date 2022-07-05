# - Running the program returns the following numbers in a list: [1, 2, 56, 32, 51, 2, 8, 92, 15]
# - Running the program returns the above numbers in a list in ascending order. The order is not hardcoded.
# - The steps seen in the flowchart are used. [1, 2, 2, 8, 15, 32, 51, 56, 92]

# lista, amit sorbarendezünk
array = [1, 2, 56, 32, 51, 2, 8, 92, 15]


# a függvényünknek megadunk 1 paramétert: a tömb, amit sorbarendezünk
def my_bubble_sort(list_to_swap):
    # az n változó egyenlő lesz a sorbarendezendő lista hosszával
    n = len(list_to_swap)
    i = 0
    # amíg az i segédváltozó kisebb, mint a lista hossza...
    while i < n - 1:
        # a j segédváltozó értékét nem növeljük
        j = 0
        # amíg a j segédváltozó értéke kisebb mint a lista hosszából kivont i segédváltozó értéke minusz egy...
        while j < n - i - 1:
            # és ha a lista j értékének megfelelő indexű eleme nagyobb,
            # mint a lista j+1 értékének megfelelő indexű eleme...
            if list_to_swap[j] > list_to_swap[j+1]:
                # akkor megcseréljük, az elemek sorrendjét
                list_to_swap[j], list_to_swap[j+1] = list_to_swap[j+1], list_to_swap[j]
                # és növeljük a j segédváltozó értékét iterációnként
                j += 1
            else:
                # máskülönben csak növeljük a j segédváltozó értékét iterációnként
                j += 1
        # addig növeljük az i segédváltozó értékét iterációnként
        i += 1
    # kiíratjuk sorbarendezett listát egy kis kísérőszöveggel
    print('Ordered list: ' + str(list_to_swap))


# meghívjük a függvényünket, átadva neki a sorbarendezni kívánt listát
my_bubble_sort(array)
