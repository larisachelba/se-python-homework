"""
    Ex. 18: Scrieti o functie care sa intoarca suma unei liste de numere
    folosind recursivitate.

    Exemplu:
        - f([1,2,3])
            ---> 6
"""


def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    elif len(numlist) == 0:
        return 0
    else:
        return numlist[0] + listsum(numlist[1:])


print(listsum([]))
