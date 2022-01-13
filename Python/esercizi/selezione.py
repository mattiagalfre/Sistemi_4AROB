voto = int(input("Scrivi il tuo voto: "))
if voto > 8:
    print("Eccellente")
elif (voto >= 7) & (voto <= 8):
    print("Buono")
elif (voto >= 6) & (voto < 7):
    print("Sufficiente")
else:
    print("Insufficiente")
