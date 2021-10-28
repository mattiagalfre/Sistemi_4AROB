"""x = 123
x = "Ciao" #viene assegnata una nuova cella ad x che contiene Ciao, 123 sarà sempre memorizzato, ma non sarà più accessibili

#GARBAGE COLLECTION: processo di pulizia degli oggetti orfani(non più accessibili)"""

#SLICING
stringa = "Classe quarta A robotica"

"""
print(f"Il primo carattere della stringa è {stringa[0]}")
print(f"L'ultimo carattere della stringa è {stringa[-1]}")
print(stringa[0:6])     #prende i caratteri dal primo indice compreso al secondo indice ESCLUSO
print(stringa[6:])      #prende i caratteri dal primo indice alla fine
print(stringa[:-2])     #prende tutta la stringa fino all'indice ESCLUSO
print(stringa[2:14:2])  #prende i caratteri dal primo indice fino al secondo indice ESCLUSO saltando ogni volta del terzo valore
print(stringa[::-1])    #inverte la stringa
"""

# stringa[15] = 'B'  -> non si può fare
#le stringhe in python sono IMMUTABILI, non si può cambiare un carattere dentro una stringa
#TypeError: 'str' object does not support item assignment

stringa_nuova = stringa[0:14] + 'B' + stringa[15:]
print(stringa_nuova)
print(f"LA STRINGA MODIFICATA E': {stringa_nuova}")

print(print)

