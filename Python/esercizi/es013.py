"""Utilizzando il modulo random (https://docs.python.org/3/library/random.html), 
simula dieci lanci di un dado per Alice e dieci lanci di un dado per Bob, mediante list comprehension. 
Il dado è a sei facce. Salva i lanci all’interno di un file, su dieci righe, 
in cui la prima colonna corrisponde ai lanci di Alice e la seconda a quelli di Bob. 
Utilizza la virgole come separatore all’interno delle righe."""

import random

f = open(".\dadi.txt", "w")

Alice = [random.randint(1, 6) for _ in range(10)]
Bob = [random.randint(1, 6) for _ in range(10)]

for k in range(10):
    f.write(f"{Alice[k]} , {Bob[k]}\n")

f.close


