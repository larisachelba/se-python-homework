"""
    Ex. 12: Scrieti un decorator pt f care sa scrie outputul lui f intr-un
    fisier, "output12.data".

    Observatii: f nu e la fel ca la ex 11.

"""


def dec(func):
    def wrapper(*args):
        file = open("output12.data", "w")
        file.write(str(func(*args)))
    return wrapper


@dec
def f(x):
    print(x)


f('output')




