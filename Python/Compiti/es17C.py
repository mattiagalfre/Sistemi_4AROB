"""Utilizza le list comprehension per generare la tavola pitagorica"""

tavola_pitaorica = [(x*y) for x in range(11) for y in range(11)]

indice1 = 0
indice2 = 11

for _ in range(11):     #si usa under-score(_) per non usare memoria inutile poichè la variabile non serve nel ciclo
    print(tavola_pitaorica[indice1:indice2])
    indice1 += 11
    indice2 += 11

#lista di liste --> matrice
tavola = [[x*y for x in range(11)]for y in range(11)]
print(tavola)

