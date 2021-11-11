"""Crea un programma che permette all'utente di inserire il suo nome(tramite input) e stampi
il nome in cui tutti i caratteri tranne il primo sono sostituita da un *"""

nome = input("Inserisci il tuo nome: ")
nomeNasc = nome[0] + ((len(nome)-1) * "*")
print(nomeNasc)
