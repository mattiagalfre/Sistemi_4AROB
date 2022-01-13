f = open(".\mask.txt", "w")     #apro il file in scrittura

ip_address=["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]     #dichiaro e inizializzo la lista

for indirizzo in ip_address:            #scrivo sul file la maschera di ogni indirizzo tramite lo slicing
    f.write(indirizzo[-3:] + "\n")

f.close()           #chiudo il file

