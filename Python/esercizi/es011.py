"""Utilizzando il modulo random, simula una partita a dadi tra due giocatori Alice e Bob.
Il dado è a sei facce. Vince colui che ottiene il punteggio più alto. Stampa il nome del vincitore"""

#MODULO = libreria
"""Moduli possono essere nativi se erano già installate insieme a python oppure non nativi quando sono librerie esterne"""

import random

dadoAlice = random.randint(1, 6)
dadoBob = random.randint(1, 6)
print(f"Dado di Alice = {dadoAlice}\nDado di Bob = {dadoBob}")
if dadoAlice > dadoBob:
    print(f"Ha vinto Alice")
elif dadoBob > dadoAlice:
    print(f"Ha vinto Bob")
else:
    print(f"Pareggio")