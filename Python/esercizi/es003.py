operazione = int(input("Inserisci il codice numerico dell'operazione che vuole eseguire: \n0: somma\n1: sottrazione\n2:moltiplicazione\n3:divisione\n"))
num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))

if operazione == 0:
    ris = num1 + num2
elif operazione == 1:
    ris = num1 + num2
elif operazione == 2:
    ris = num1 * num2
else:
    ris = num1 / num2

print(f"Il risultato è {ris}")