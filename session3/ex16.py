"""
    Ex. 16: Scrieti o functie upper care sa intoarca un text uppercase complet,
    primind un parametru my_str (string).
    --> f('cmi') --> 'CMI'

    Scrieti o functie lower care sa intoarca un text lowercase complet,
    primind un parametru my_str (string).
    --> f('CMI') --> 'cmi'

    Veti primi un input de la tastatura, un string.

    Scrieti o alta functie call_changers, care sa primeasca o functie ca si
    parametru, iar daca inputul are un numar par de caractere, va printa inputul
    cu uppercase, altfel, va printa inputut lowercase.

    Exemplu:
        - veti primi input: 'ceva'
            ---> CEVA
        - veti primi input: 'cEVa1'
            ---> ceva1
"""


def upper(my_str):
    return ''.join([c.upper() for c in my_str])


def lower(my_str):
    return ''.join([c.lower() for c in my_str])


def call_changers(func, x):
    return func(x)


my_string = input()

if len(my_string) % 2 == 0:
    print(call_changers(upper, my_string))
else:
    print(call_changers(lower, my_string))


