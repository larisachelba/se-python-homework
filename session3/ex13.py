"""
    Ex. 13: Scrieti un decorator care sa modifice modul de functionare
    al functiei f. Puteti alege voi cum. Momentan, f intoarce 'cmi', un exemplu
    ar fi sa intoarca 'CmI' dupa aplicarea decoratorului.

"""


def deco(func):
    def wrapper():
        return ''.join([c.upper() for c in func()])
    return wrapper


@deco
def f():
    return 'cmi'


print(f())
