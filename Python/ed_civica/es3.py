import matplotlib.pyplot as plt

mese = []
temp_media_mese = []
giorni_giacca_mese = []
giorni_scuola_mese = []
giorni_videogame_mese = []

f = open(".\es3.csv", "r")
righe = f.readlines()
righe.pop(0) 


for riga in righe:
    dato = riga.split(",")
    mese.append(dato[0])
    temp_media_mese.append(float(dato[1]))
    giorni_giacca_mese.append(int(dato[2]))
    giorni_scuola_mese.append(int(dato[3]))
    giorni_videogame_mese.append(int(dato[4]))
    
f.close()


fig, axs = plt.subplots(nrows = 2, ncols = 2, figsize = (30, 35))
plt.subplots_adjust(None, None, None, None, 0.2, 0.4)

axs[0][0].plot(mese, temp_media_mese, 'rd-', linewidth = 3, markersize = 10)
axs[0][0].set_title("Media climatica Cuneo 2020", fontsize = 25, fontweight = 'bold')
axs[0][0].set_ylabel("Temperatura media [°C]")
axs[0][0].set_xlabel("Mese")
axs[0][0].grid()

axs[0][1].plot(mese, giorni_giacca_mese,'gs-', linewidth = 2, markersize = 10)
axs[0][1].set_title("Giorni in cui indossare una giacca 2020", fontsize = 25, fontweight = 'bold')
axs[0][1].set_ylabel("Giorni in cui si addossa la giacca")
axs[0][1].set_xlabel("Mese")
axs[0][1].grid()

axs[1][0].plot(mese, giorni_scuola_mese,'rd-', linewidth = 2, markersize = 10)
axs[1][0].set_title("Giorni scolastici 2020", fontsize = 25, fontweight = 'bold')
axs[1][0].set_ylabel("Giorni in cui si va a scuola")
axs[1][0].set_xlabel("Mese")
axs[1][0].grid()

axs[1][1].plot(mese, giorni_videogame_mese,'gs-', linewidth = 2, markersize = 10)
axs[1][1].set_title("Giorni a cui si gioca ai videogame 2020", fontsize = 25, fontweight = 'bold')
axs[1][1].set_ylabel("Giorni a cui si gioca ai videogame")
axs[1][1].set_xlabel("Mese")
axs[1][1].grid()

plt.show()