alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
#la lista è visibile da tutti, ma nessuno può modificarla

def criptare(stringa, chiave):
    stringaCriptata = ""
    for carattere in stringa:
        j = 0
        while carattere != alfabeto[j] and j < 28:
            j += 1

        stringaCriptata = stringaCriptata + alfabeto[((j+chiave) % 27)]

    return stringaCriptata

def decriptare(stringaCriptata, chiave):
    stringa = ""
    for carattere in stringaCriptata:
        j = 0
        while carattere != alfabeto[j] and j < 28:
            j += 1

        stringa = stringa + alfabeto[((j-chiave) % 27)]

    return stringa

def main():
    scelta = int(input("Criptare o decriptare? (0 o 1): "))

    if scelta == 0:
        chiave = int(input("Inserisci il numero di caratteri shiftati per il linguaggio: "))
        stringa = input("Inserisci una stringa: ")
        stringa = stringa.upper()
        print(f"Stringa iniziale: '{stringa}'\n")
        stringaCriptata = criptare(stringa, chiave) 
        print(f"Stringa criptata: '{stringaCriptata}'\n")

    elif scelta == 1:
        chiave = int(input("Inserisci il numero di caratteri shiftati per il linguaggio: "))
        stringaCriptata = input("Inserisci una stringa criptata: ")
        stringaCriptata = stringaCriptata.upper()
        print(f"Stringa iniziale: '{stringaCriptata}'\n")
        stringa = decriptare(stringaCriptata, chiave)   
        print(f"Stringa decriptata: '{stringa}'\n")

    elif scelta != 1 and scelta != 0:
        print("CODICE INVALIDO!")

if __name__ == "__main__":
    main()

    
