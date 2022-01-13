"""Scrivere un programma che data una lista qualsiasi la trasformi in un
dizionario avente come chiavi gli indici della lista e come valori gli
elementi."""

lista = [5, 6, 8, 7]
dizionario = {}

for k, elemento in enumerate(lista):
    dizionario[k] = elemento

"""
dizionario = {x : elemento for x, elemento in enumerate(lista)}
"""

print(dizionario)
