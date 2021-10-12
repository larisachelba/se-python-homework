"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti daca acel string este palindrom, folosind tipul de date
    boolean (True, False)

    Observatii:
        - palindrom: stringul se citeste la fel de la stranga la dreapta,
        si de la dreapta la stanga

    exemplu:
        Veti primi: 'center'
        Veti printa: False

        Veti primi: 'cojoc'
        Veti printa: True
"""
x = input()
y = ""

for i in range(len(x)):
    y += x[-i-1]
# a = reversed(x)
# for c in a:
#     print(c)
if x == y:
    print(True)
else:
    print(False)
