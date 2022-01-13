"""Scrivi un programma Python che chieda all’utente i suoi dati anagrafici (nome, cognome, data di nascita), 
li salvi all’interno di un dizionario e infine salvi il dizionario su un file, elemento per elemento"""

dati = {"nome": input("Inserisci il tuo nome: "), "cognome": input("Inserisci il tuo cognome: "), "data di nascita": input("Inserisci la tua data di nascita: ")}
f = open("./DatiAnagrafici.txt", "w")
for chiave in dati:
    f.write(dati[chiave] + "\n")
f.close()