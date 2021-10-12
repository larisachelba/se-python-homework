"""
    Veti primi un string de la tastatura, care reprezinta o succesiune de
    paranteze rotunde, drepte si acolade. Va trebui sa spuneti daca parantezele
    sunt inchise corect, sau nu. (boolean - True|False)

    exemplu:
        Veti primi: '(([])){}'
        Veti printa: True

        Veti primi: '(()]'
        Veti printa: False
"""
x = input()
x = [c for c in x]
l1 = []
y = []
z = 0
for i, e in enumerate(x):
    if x[i] == '(':
        l1.append(x[i])
    if x[i] == ')':
        if '(' in l1:
            l1.pop(l1.index('('))
        else:
            z = 1
            break
    if x[i] == '[':
        l1.append(x[i])
    if x[i] == ']':
        if '[' in l1:
            l1.pop(l1.index('['))
        else:
            z = 1
            break
    if x[i] == '{':
        l1.append(x[i])
    if x[i] == '}':
        if '{' in l1:
            l1.pop(l1.index('{'))
        else:
            z = 1
            break
if not l1 and z != 1:
    print(True)
else:
    print(False)
