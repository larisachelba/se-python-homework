"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa spuneti daca acel numar este palindrom, folosind tipul de date
    boolean (True, False)

    Observatii:
        - palindrom: numarul este acelasi de la stranga la dreapta,
        si de la dreapta la stanga

    exemplu:
        Veti primi: 12321
        Veti printa: True

        Veti primi: 1232
        Veti printa: False
"""
x = input()
x = int(x)
z = x
y = 0
while x > 0:
    i = x % 10
    y = y * 10 + i
    x = x//10
if z == y:
    print(True)
else:
    print(False)
