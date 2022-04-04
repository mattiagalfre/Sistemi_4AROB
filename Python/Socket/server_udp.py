import socket
#                      IPV4              UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("192.168.0.0", 5000))     #legare il server con IP e porta        da fare solo su SERVER

while True:
    dati, ind_client = s.recvfrom(4096)    #4096 è la dimensione in byte del buffer di ricezione
    print(f"{dati.decode()} ricevuti da {ind_client}")      #dati.decode() -> riconverte i dati in una stringa
