"""Utilizza il modulo random per simulare una partita a dadi tra Alice e Bob."""

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