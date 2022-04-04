import socket
#                      IPV4              UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    stringa = input("Inserisci una stringa: ")
    s.sendto(stringa.encode(), ("192.168.0.119", 5000))   #(dati in binario, (destinatario))            stringa.encode() -> converte i dati in binario 