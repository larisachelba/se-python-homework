"""
    Veti primi un string de la tastatura.
    Va trebui sa printati numarul de vocale si numarul de consoane din
    acel string.

    exemplu:
        Veti primi: 'center'
        Veti printa:
        2 (pentru vocale)
        4 (pentru consoane)
"""
x = input()
v = set('aeiouAEIOU')
vocale = 0
consoane = 0
for i in x:
    if v.__contains__(i):
        vocale += 1
    else:
        consoane += 1
print(vocale, 'vocale ')
print(consoane, 'consoane')