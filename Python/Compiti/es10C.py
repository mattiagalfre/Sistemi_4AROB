"""Scrivi un programma che permetta all'utente di inserire le coordinate di due punti del piano cartesiano
I punti devono essere salvati all'interno di tuple. Stampa la distanza euclidea tra i due punti."""

import math

punto1 = (float(input("Inserisci l'ascissa del primo punto: ")), float(input("Inserisci l'ordinata del primo punto: ")))
punto2 = (float(input("Inserisci l'ascissa del secondo punto: ")), float(input("Inserisci l'ordinata del secondo punto: ")))

distanza = math.sqrt((punto2[0] - punto1[0])**2 + (punto2[1] - punto1[1])**2)
print(f"La distanza euclidea tra i due punti è {distanza}")