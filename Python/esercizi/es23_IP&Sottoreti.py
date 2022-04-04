def bin2dec(valBin):
    valDec = 0
    for i, k in enumerate(valBin):
        valDec =  valDec + 2**(len(valBin) - 1 - i) * int(k)
        
    return valDec

def dec2bin(valDec, nBit):
    valBin = bin(valDec)[2:]
    valBin = "0" * (nBit - len(valBin)) + valBin
    return valBin 

def IP_dec2bin(indirizzoDec):
    valBin = ""
    gruppi = indirizzoDec.split(".")
    for gruppo in gruppi:
        valBin += dec2bin(int(gruppo),8)
    
    return valBin

def IP_bin2dec(indirizzoBin):
    valDec, nBit = "", 8
    for num in range(0, 32, nBit):
        valDec += str(bin2dec(indirizzoBin[num : num + nBit])) + "."
    
    return valDec[:-1]

def controlloIP_rete(IP_rete, subnetMask):
    IP_reteBin = IP_dec2bin(IP_rete)
    bitHost = 32 - int(subnetMask)

    if IP_reteBin[int(subnetMask):] == bitHost * "0":
        controllo = True
    else:
        controllo = False

    return controllo

def broadcastBin(IP_rete, subnetMask):
    bitHost = 32 - subnetMask
    IP_reteBin = IP_dec2bin(IP_rete)
    IP_broadcastBin = IP_reteBin[:-bitHost]
    for _ in range(bitHost):
        IP_broadcastBin += "1"

    return IP_broadcastBin

def broadcastDec(IP_rete, subnetMask):
    bitHost = 32 - subnetMask
    IP_reteBin = IP_dec2bin(IP_rete)
    IP_broadcastBin = IP_reteBin[:-bitHost]
    for _ in range(bitHost):
        IP_broadcastBin += "1"
    IP_broadcastDec = IP_bin2dec(IP_broadcastBin)

    return IP_broadcastDec

def primoIPBin(IP_rete):
    IP_reteBin = IP_dec2bin(IP_rete)
    primoIPBin = IP_reteBin[:-1] + "1"

    return primoIPBin

def primoIPDec(IP_rete):
    IP_reteBin = IP_dec2bin(IP_rete)
    primoIPBin = IP_reteBin[:-1] + "1"
    primoIPDec = IP_bin2dec(primoIPBin)

    return primoIPDec

def ultimoIPBin(IP_broadcast):
    ultimoIPBin = IP_broadcast[:-1] + "0"

    return ultimoIPBin

def ultimoIPDec(IP_broadcast):
    ultimoIPBin = IP_broadcast[:-1] + "0"
    ultimoIPDec = IP_bin2dec(ultimoIPBin)

    return ultimoIPDec

def riconosciSubnetMask(subnetMask):
    if subnetMask[0] == "/":
        mascheraUtile = subnetMask[1:]
    elif (subnetMask[0] > 0 and subnetMask[0] < 10):
        """
        if subnetMask[3] == ".":
            maskBin = IP_dec2bin(subnetMask)
            k = 0
            tro = False
            while (k < 33 and tro == False):
                if(maskBin[k] == "0"):
                    tro = True
                k += 1
            mascheraUtile = k - 1
        """
    else:
        print("Subnet Mask non valida")
        mascheraUtile = None

    return mascheraUtile


def main():
    IP_rete = input("Inserisci l'IP della rete: ")
    subnetMask = input("Inserisci n della subnet mask nella forma '/n': ")

    if(controlloIP_rete(IP_rete, int(subnetMask)) == True):
        print("\nIP di rete corretto\n")
    else:
        while(controlloIP_rete(IP_rete, subnetMask) == True):
            print("\nIP di rete non corretto, Reinserisci: ")
            IP_rete = input()

    print("IP di rete: " + IP_rete) 
    print("IP di rete binario: " + IP_dec2bin(IP_rete))  
    print("IP di broadcast: " + broadcastDec(IP_rete, int(subnetMask)))
    print("IP di broadcast: " + broadcastBin(IP_rete, int(subnetMask)))
    print("Primo IP utilizzabile: " + primoIPDec(IP_rete))
    print("Ultimo IP utilizzabile: " + ultimoIPDec(broadcastBin(IP_rete, int(subnetMask))))

if __name__ == "__main__":
    main()