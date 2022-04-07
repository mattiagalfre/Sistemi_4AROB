import matplotlib.pyplot as plt

mese = []
mese_n = []
ore_studio_giornaliere = []
media_voti = []

f = open(".\studio.csv", "r")
righe = f.readlines()
righe.pop(0) 


for riga in righe:
    dato = riga.split(",")
    mese.append(dato[0])
    mese_n.append(int(dato[1]))
    ore_studio_giornaliere.append(float(dato[2]))
    media_voti.append(float(dato[3]))
    
f.close()

#due grafici in due figure diverse
"""
#PRIMO GRAFICO
fig, ax = plt.subplots(figsize = (10, 6))    
ax.plot(mese, ore_studio_giornaliere, 'rd-', linewidth = 3, markersize = 20)
ax.set_title("Ore di studio giornaliere", fontsize = 25, fontweight = 'bold')
ax.set_ylabel("Ore di studio giornaliere")
ax.set_xlabel("Mese")
ax.grid()
plt.show()

#SECONDO GRAFICO
fig, ax = plt.subplots(figsize = (10, 6))    
ax.plot(mese, media_voti,'gs-', linewidth = 2, markersize = 20)
ax.set_title("Media dei voti", fontsize = 25, fontweight = 'bold')
ax.set_ylabel("Media dei voti")
ax.set_xlabel("Mese")
ax.grid()
plt.show()
"""

#due grafici in una sola figura
fig, axs = plt.subplots(nrows = 2, ncols = 1, figsize = (10, 20)) 

axs[0].plot(mese, ore_studio_giornaliere, 'rd-', linewidth = 3, markersize = 20)
axs[0].set_title("Ore di studio giornaliere", fontsize = 25, fontweight = 'bold')
axs[0].set_ylabel("Ore di studio giornaliere")
axs[0].set_xlabel("Mese")
axs[0].grid()

axs[1].plot(mese, media_voti,'gs-', linewidth = 2, markersize = 20)
axs[1].set_title("Media dei voti", fontsize = 25, fontweight = 'bold')
axs[1].set_ylabel("Media dei voti")
axs[1].set_xlabel("Mese")
axs[1].grid()

plt.savefig("grafico.png")
plt.savefig("grafico.pdf")
plt.show()