"""Crea una funzione Python che data una lista di numeri, ritorni il suo valore massimo e il suo valore minimo"""

numeri = [5, 4, 3, 8, 6, 9, 10, 1.2]
max = numeri[0]
min = numeri[0]

for numero in numeri[1:]:
    if numero > max:
        max = numero
    if numero < min:
        min = numero
print(f"Il massimo nella lista è {max} e il minimo nella lista è {min}")