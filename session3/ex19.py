"""
    Ex. 19: Scrieti o functie care primeste un string ca si parametru,
    creeaza un fisier cu numele parametrului primit (.json) si scrie in el
    un dictionar de 4 elemente aleatoare unde key = int, iar value = string,
    iar stringul sa aiba intre 3 si 6 caractere si key sa fie intre 0 si 10.

    Exemplu:
        f('ceva')
        ---> generez ceva.json ca si fisier
        ---> generez un dictionar
            {
                1: 'blabla',
                5: 'cmi',
                7: 'cmi22',
                10: 'balqef'
            }

"""
import json
import random


def func(file_name):
    file = open(file_name + ".json", "w")
    d1 = {}
    my_str = 'asdfghjklzxcvbnmqwertyuiop'
    for i in range(4):
        j = random.choice(range(11))
        while j in d1.keys():
            j = random.choice(range(11))
        d1[j] = "".join(random.choices(my_str, k=random.choice(range(3, 6))))
    print(d1)
    file.write(json.dumps(d1))


func('output19')
