"""
mappa d*d     d = 4

piastrelle libere(1) o piastrelle vuote(0)
lista di liste:
[[0,0,0,1], [1,0,0,1], [0,0,0,0], [1,1,1,0]]

Robot si muove solo su piastrelle libere, non in diagonale

Assegno ad ogni cella libera un numero intero e costruisco un dizionario delle adiacenze:
{indice della cella : [celle in cui si può muovere il robot]}       esempio: {0:[1], 1:[0,2,3], 2:[1,4],...}
"""
import random, sys, pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
GREEN = (0, 255, 0)

def assegnaCelleVuote(mappa):
    dizionario,n,dim = {},0,len(mappa)
    for k in range(dim):
        for j in range(dim):
            if mappa[k][j] == 0:
                dizionario[n] = [k,j]
                n+=1
    return dizionario

def controlloBordi(lista,dim):
    dizioBool,ritorno= {"su":None,"giu":None,"dx":None,"sx":None},[]
    if lista[0] == 0 :
        dizioBool["su"] = False
    if lista[1] == 0:
        dizioBool["sx"] = False
    if lista[0] == dim-1:
        dizioBool["giu"] = False
    if lista[1] == dim-1:
        dizioBool["dx"] = False
    for chiave in dizioBool:
        if dizioBool[chiave] == False: ritorno.append(chiave)
    return ritorno

def trovaChiave(dizioVuote,x,y):
    for chiave in dizioVuote:
        if dizioVuote[chiave] == [x,y]: return chiave
    return -1

def controlloFinale(opzioniSbagliate,mappa,dizioVuote,chiave):
    listaFinale = []
    if "su" not in opzioniSbagliate: 
        chiaveTrovata = trovaChiave(dizioVuote, dizioVuote[chiave][0]-1, dizioVuote[chiave][1])
        if  chiaveTrovata != -1: 
            listaFinale.append(chiaveTrovata)
    if "giu" not in opzioniSbagliate:
        chiaveTrovata = trovaChiave(dizioVuote, dizioVuote[chiave][0]+1, dizioVuote[chiave][1])
        if  chiaveTrovata != -1: 
            listaFinale.append(chiaveTrovata)
    if "dx" not in opzioniSbagliate:
        chiaveTrovata = trovaChiave(dizioVuote, dizioVuote[chiave][0], dizioVuote[chiave][1]+1)
        if  chiaveTrovata != -1:
            listaFinale.append(chiaveTrovata)
    if "sx" not in opzioniSbagliate:
        chiaveTrovata = trovaChiave(dizioVuote, dizioVuote[chiave][0], dizioVuote[chiave][1]-1)
        if  chiaveTrovata != -1:
            listaFinale.append(chiaveTrovata)
    return listaFinale

def creaMappa(dim):
    mat = [[0]*dim for _ in range(dim)]
    for k in range(dim):
        for j in range(dim):
            x = random.choice([0, 0, 1])
            mat[k][j] = x
            if j == 0 and k == 0:
                mat[k][j] = 0
    return mat

def trovaAdiacenze(mappa,dizioVuote):
    dizioAdiacenze,opzioniSbagliate = {},[]
    for chiave in dizioVuote:
        opzioniSbagliate = controlloBordi(dizioVuote[chiave],len(mappa))
        print(f"{chiave}: {opzioniSbagliate}")
        dizioAdiacenze[chiave] = controlloFinale(opzioniSbagliate,mappa,dizioVuote,chiave)
    return dizioAdiacenze

def main():
    dimMappa = 10
    mappa = creaMappa(dimMappa)
    print(mappa)
    dizioVuote = assegnaCelleVuote(mappa)
    dizioAdiacenze = trovaAdiacenze(mappa, dizioVuote)
    #print(f"dizionario delle celle il cui si puo andare: {dizioVuote}")
    #print(f"dizionario adiacenze: {trovaAdiacenze(mappa, dizioVuote)}")

    
    pygame.init()
    sizeCella = 50

    widthCampo, heightCampo = dimMappa*sizeCella,dimMappa*sizeCella

    size=(widthCampo, heightCampo)
    screen = pygame.display.set_mode(size)
    print(mappa)
    pygame.display.set_caption("Campo di gioco")
    

    #ball = pygame.image.load("./intro_ball.gif")
    #ballrect = ball.get_rect()
    xBall = 0
    yBall = 0

    while True:       
        for riga in range(len(mappa)):
            for colonna in range(len(mappa)):
                color = WHITE
                if mappa[riga][colonna] == 1:
                    color = RED
                pygame.draw.rect(screen, color, [(sizeCella) * colonna,(sizeCella) * riga,sizeCella,sizeCella])

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN: 
                if event.__dict__["unicode"] == "w":
                    if (yBall - 1) >= 0:
                        if mappa[yBall - 1][xBall] == 0:
                            yBall = yBall - 1
                            print(f"[{yBall}, {xBall}]")
                elif event.__dict__["unicode"] == "s":
                    if (yBall + 1) <= (dimMappa - 1):
                        if mappa[yBall + 1][xBall] == 0:
                            yBall = yBall + 1
                            print(f"[{yBall}, {xBall}]")
                elif event.__dict__["unicode"] == "d":
                    if (xBall + 1) <= (dimMappa - 1):
                        if mappa[yBall][xBall + 1] == 0:
                            xBall = xBall + 1 
                            print(f"[{yBall}, {xBall}]")
                elif event.__dict__["unicode"] == "a":
                    if (xBall - 1) >= 0:
                        if mappa[yBall][xBall - 1] == 0:
                            xBall = xBall - 1
                            print(f"[{yBall}, {xBall}]")
        pygame.draw.circle(screen, GREEN, [((xBall * sizeCella) + (sizeCella / 2)), ((yBall * sizeCella) + (sizeCella / 2))], (sizeCella / 2) - 3)

        pygame.display.flip()

if __name__ == "__main__":
    main()
