"""
    Veti primi un string de la tastatura.
    Va trebui sa printati un tuplu care sa contina toate literele acelui string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: ('c', 'm', 'i')
"""
x = input()
l1 = []
for i in x:
    l1.append(i)
print(tuple(l1))
