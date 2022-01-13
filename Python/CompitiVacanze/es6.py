"""Il file covid-19_gen1.txt contiene la sequenza genomica RNA di un
virus SARS-COV-2. L'RNA è una sequenza in cui si alternano 4
simboli (detti nucleotidi): A, T, C, G. L'RNA del virus SARS-COV-2
contiene 29903 nucleotidi. Leggi covid-19_gen1.txt il file e crea un
dizionario Python avente come chiavi i nucleotidi A, T, C, G e come
valori i rispettivi conteggi."""

def main():
    f = open("./covid-19_gen1.txt", "r")
    righe = f.readlines()
    rna = {"A":0, "T":0, "C":0, "G":0}
    lista = ["A", "T", "C", "G"]

    for riga in righe:
        for elemento in lista:
            if elemento == "A":
                rna["A"] += riga.count(elemento)
            elif elemento == "T":
                rna["T"] += riga.count(elemento)
            elif elemento == "C":
                rna["C"] += riga.count(elemento)
            elif elemento == "G":
                rna["G"] += riga.count(elemento)
        
    f.close()
    print(rna)

if __name__ == "__main__":
    main()