"""
    Ex. 6: Scrieti o functie cu un singur parametru (string) care
    intoarce un string cu toate literele stringului primit +1 (adica urmatoarea
    litera din alfabet)

    Raspuns:
        - func('aabbcc')
            ---> 'bbccdd'
"""


def func(string):
    new_string = ''
    for character in string:
        new_string += chr(ord(character) + 1)
    return new_string


print(func(input()))
