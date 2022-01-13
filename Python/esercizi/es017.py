def main():
    f = open("./es17.txt", "w")

    risposta = "si"

    while risposta == "si":
        nome = input("Inserisci il nome dell'alunno: ")
        nomeNasc = nome[0] + ((len(nome)-1) * "*")
        voto = -1
        while voto < 0 or voto > 10:
            voto = int(input("Inserisci il voto di condotta dell'alunno (da 0 a 10): "))
        
        f.write(f"{nomeNasc}, {voto} \n")

        risposta = input("Vuoi inserire altri alunni? ('si' per continuare): ")

    print("Dati stampati su file")

if __name__ == "__main__":
    main()
