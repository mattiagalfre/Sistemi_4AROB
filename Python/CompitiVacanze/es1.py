#Scrivere un programma che data una lista qualsiasi ne elimini i duplicati.

lista = [5, 6, 8, 7, 6]
"""
risposta = "si"
while risposta == "si":
    newElem = input("Inserisci il nuovo elemento della lista: ")
    lista.append(newElem)
    risposta = input("Vuoi inserire altri elementi? ('si' per continuare): ")"""

listaTemp = []
for elementoCurr in lista:
    occorrenze = 0
    for elemento in listaTemp:
        if (elementoCurr == elemento):
            occorrenze = occorrenze + 1
    if (occorrenze == 0):
        listaTemp.append(elementoCurr)

lista = listaTemp
print(lista)
