"""
    Veti primi un string de la tastatura.
    Va trebui sa afisati acel string cu o litera mare/una mica.

    exemplu:
        Veti primi: 'center'
        Veti printa: 'CeNtEr'
"""
x = input()
y = ""
for i in range(len(x)):
    if i % 2 == 0:
        y += (x[i].upper())
    else:
        y += x[i].lower()
print(y)
