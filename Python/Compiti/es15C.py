"""Data una lista di stringhe estrai da essa la lista di stringhe che sono palindrome 
e la lista di stringhe che hanno iniziale maiuscola."""

parole = ["ciao", "Mattia", "anna", "Cavallo", "gatto"]
palidrome = [parola for parola in parole if parola == parola[::-1]]
print(f"Parole palindrome: {palidrome}")
maiuscola = [parola for parola in parole if parola[0] >= "A" and parola[0] <= "Z"]
print(f"Parole che iniziano con maiuscola: {maiuscola}")