classi = ["4arob", "3arob", "5brob", "4achi", "3ainf"]
indirizzi = {"rob": "Smart Robot", "chi": "Chimica", "inf": "Informatica"}

indice = 0
for indice, classe in enumerate(classi):
    indirizzo = indirizzi[classe[-3:]]
    print(f"Posizione {indice} nella lista: ")
    print(f"La classe {classe}  è dell'indirizzo {indirizzo}", end = "\n\n")
