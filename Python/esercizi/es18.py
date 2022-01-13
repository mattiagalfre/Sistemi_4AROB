n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))
lista = []
lista.append((n1**2)+(n2**2))
lista.append((n1+n2)**2)
lista.append((n1**2)-(n2**2))
lista.append((n1-n2)**2)
print(lista)