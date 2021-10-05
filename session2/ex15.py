"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1
"""
from operator import contains

x = input()
vocale = set('aeiouAEIOU')
count = 0
for i in x:
    if vocale.__contains__(i):
        count = count + 1
print(count)
