"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati un strign aleator cu numarul de caractere egal
    cu numarul intreg primit.

    exemplu:
        Veti primi: 5
        Veti printa: 'ashdj' (poate fi orice alt string)
"""

import random

x = int(input())
y = ""
l1 = ['a', 's', 'd', 'f', 'g', 'h', 'j']
for i in range(x):
    y += random.choice(l1)
print(y)