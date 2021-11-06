"""
    Ex. 7: Scrieti o functie care sa primeasca trei parametri
        - prefix (string)
        - word (string)
        - suffix (string)
    Si trebuie sa intoarca cuvantul cu prefixul si sufixul adaugate.

    Raspuns:
        - pentru prefix = 'a', suffix = 'b' si word = 'x'
            ---> 'axb'

    Observatii:
        - functia trebuie sa aiba MAXIM 1 linie de cod ca si body
"""


def func(pref, word, suf):
    return pref + word + suf


prefix = str(input('Give me the prefix\n'))
word = str(input('Give me the word\n'))
suffix = str(input('Give me the suffix\n'))

print(func(prefix, word, suffix))
