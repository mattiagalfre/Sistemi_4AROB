import socket
#                      IPV4              UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("192.168.0.124", 5000))     #legare il server con IP e porta        da fare solo su SERVER

while True:
    dati, ind_client = s.recvfrom(4096)
    print(f"{dati.decode()} ricevuti da {ind_client}") 
    stringa = input("Inserisci una stringa: ")
    s.sendto(stringa.encode(), ("192.168.0.119", 5000))
    