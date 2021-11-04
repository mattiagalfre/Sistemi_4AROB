"""Crea un programma in Python in cui assegni una parola di almeno 8 lettere a una variabile stringa 
e poi stampi tutta la parola con un carattere ? al posto della terza lettera."""
stringa = "Computer"
print(stringa)
stringa_nuova = stringa[:2] + '?' + stringa[3:]
print(f"LA STRINGA MODIFICATA E': {stringa_nuova}")