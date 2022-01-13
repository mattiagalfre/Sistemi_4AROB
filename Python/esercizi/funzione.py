def somma_moltiplicazione(x, y):
    somma = x + y
    moltiplicazione = x * y
    return somma, moltiplicazione       #posso restituire più variabili insieme
    #return {"somma":somma, "moltiplicazione":moltiplicazione}

#lamba function
somma_moltiplicazione_2 = lambda x, y: (x+y, x*y)
#                            parametri: codice
a = 10
b = 4
s, m = somma_moltiplicazione_2(a, b)
print(s)
#print(somma_moltiplicazione(a, b))