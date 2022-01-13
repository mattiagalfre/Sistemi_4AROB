"""Il file prezzi.csv (separatore ;) contiene le serie storiche mensili dei
prezzi di alcuni generi alimentari dal Settembre 2011 a Dicembre
2016. Immagina una spesa costituita da 5 generi alimentari a tua
scelta e crea una lista contenente la serie storica del prezzo della tua
spesa ottenuta sommando i prezzi dei generi alimentari scelti.
Calcola mese / anno in cui la tua spesa ha costi minimi e massimi."""
import sys

prezzoSpesa = []
listaMesi = []

f = open("./prezzi.csv", "r")

prodotti = []
for i in range(5):
    prodotti.append(int(input(f"Inserisci l'indice del {i+1}: ")))

righe = f.readlines()
righe.pop(0)

for riga in righe:
    somma = 0
    campi = riga.split(";")
    listaMesi.append(campi[1] + " " + campi[0])
    for prodotto in prodotti:
        somma += float(campi[prodotto])
    prezzoSpesa.append(somma)

print(prezzoSpesa)
print(listaMesi)

prezzoMin = 10000
prezzoMax = 0
iMin = None
iMax = None

for i, prezzo in enumerate(prezzoSpesa):
    if prezzo < prezzoMin:
        prezzoMin = prezzo
        iMin = i
    if prezzo > prezzoMax:
        prezzoMax = prezzo
        iMax = i

print(f"\n\nLa spesa ha un prezzo minimo di {prezzoMin:.2f}€ nel mese di {listaMesi[iMin]} \n")
print(f"La spesa ha un prezzo massimo di {prezzoMax:.2f}€ nel mese di {listaMesi[iMax]} \n")

