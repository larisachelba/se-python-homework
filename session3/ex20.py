"""
    Ex. 20: Deschideti fisierul .json creat la exercitiul anterior, cititi
    continutul si returnati un dictionar (dictionarul de acolo).

    Toate astea le veti face intr-o functie read_from_file(file), unde
    file este numele fisierului primit dat ca parametru.
"""
import json


def read_from_file():
    file = open("output19.json", "r")
    return json.loads(file.read())


print(read_from_file())