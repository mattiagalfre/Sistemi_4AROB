"""Crea un programma che data una lista di stringhe, ritorni la stringa più lunga della lista"""

parole = ["ciao", "stella", "re"]

print(parole)
max = parole[0]
for parola in parole[1:]:
    if len(parola) > len(max):
        max = parola
print(f"La parola più lunga è {max}")