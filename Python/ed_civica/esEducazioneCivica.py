import matplotlib.pyplot as plt
import numpy as np

annoAnomalia = []
anomalia = []

f = open(".\Temperature_Anomaly.csv", "r")
righe = f.readlines()
for _ in range(5):
    righe.pop(0)

for riga in righe:
    dato = riga.split(",")
    annoAnomalia.append(int(dato[0]))
    anomalia.append(float(dato[1]))
    
f.close()

fig, ax = plt.subplots(figsize = (28, 7)) 
plt.xticks(rotation=90)
ax.bar(annoAnomalia, anomalia)
ax.set_title("Temperature Anomaly", fontsize = 30, color = "b", fontweight = "bold")
ax.set_xlabel("YEAR", color = "g", fontweight = "bold")
ax.set_xticks(np.arange(1880, 2020, 2))
ax.set_ylabel("GRADES (°C)", color = "r", fontweight = "bold")
ax.set_yticks(np.arange(-0.5, 1, 0.1))
ax.annotate("max", xy = (2016, 0.91), xytext = (2008, 0.9), arrowprops = dict(facecolor = "r", shrink = 5))
ax.grid()

plt.savefig("TemperatureAnomaly.png")
plt.show()

fig, ax = plt.subplots(figsize = (28, 7)) 
plt.xticks(rotation=90)
ax.plot(annoAnomalia, anomalia, "co")
ax.set_title("Temperature Anomaly", fontsize = 30, color = "b", fontweight = "bold")
ax.set_xlabel("YEAR", color = "g", fontweight = "bold")
ax.set_xticks(np.arange(1880, 2020, 2))
ax.set_ylabel("GRADES (°C)", color = "r", fontweight = "bold")
ax.set_yticks(np.arange(-0.5, 1, 0.1))
ax.annotate("max", xy = (2016, 0.91), xytext = (2008, 0.9), arrowprops = dict(facecolor = "r", shrink = 5))
ax.grid()

plt.savefig("TemperatureAnomalyDisp.png")
plt.show()

#####################################################################

annoCO2 = []
totale = []
gasFuel = []
liquidFuel = []
solidFuel = []
cement = []
gasFlaring = []
perCapita = []

f = open(".\CO2_emissions.csv", "r")
righe = f.readlines()
righe.pop(0)

for riga in righe:
    dato = riga.split(",")
    annoCO2.append(int(dato[0]))
    totale.append(int(dato[1]))
    gasFuel.append(int(dato[2]))
    liquidFuel.append(int(dato[3]))
    solidFuel.append(int(dato[4]))
    cement.append(int(dato[5]))
    gasFlaring.append(int(dato[6]))
    if(dato[7] == "\n"):
        perCapita.append(0)
    else:
        perCapita.append(dato[7])
   
f.close()

fig, axs = plt.subplots(nrows=2, ncols=3, figsize = (20, 12), layout="constrained")

axs[0][0].plot(annoCO2, gasFuel,  "b-")
axs[0][0].set_title("GAS FUEL EMISSION", color = "g", fontsize = 15, fontweight = "bold")
axs[0][0].set_ylabel("TONS", color = "r")
axs[0][0].set_xticks(np.arange(1750, 2011, 20))
axs[0][0].set_yticks(np.arange(0, 4000, 175))
axs[0][0].grid()

axs[0][1].plot(annoCO2, liquidFuel,  "c-")
axs[0][1].set_title("LIQUID FUEL EMISSION", color = "r", fontsize = 15, fontweight = "bold")
axs[0][1].set_ylabel("TONS", color = "r")
axs[0][1].set_xticks(np.arange(1750, 2011, 20))
axs[0][1].set_yticks(np.arange(0, 4000, 175))
axs[0][1].grid()

axs[0][2].plot(annoCO2, solidFuel,  "g-")
axs[0][2].set_title("SOLID FUEL EMISSION", color = "y", fontsize = 15, fontweight = "bold")
axs[0][2].set_ylabel("TONS", color = "r")
axs[0][2].set_xticks(np.arange(1750, 2011, 20))
axs[0][2].set_yticks(np.arange(0, 4000, 175))
axs[0][2].grid()

axs[1][0].plot(annoCO2, cement,  "m-")
axs[1][0].set_title("CEMENT EMISSION", color = "b", fontsize = 15, fontweight = "bold")
axs[1][0].set_ylabel("TONS", color = "r")
axs[1][0].set_xticks(np.arange(1750, 2011, 20))
axs[1][0].set_yticks(np.arange(0, 4000, 175))
axs[1][0].grid()

axs[1][1].plot(annoCO2, gasFlaring,  "r-")
axs[1][1].set_title("GAS FLARING EMISSION", color = "b", fontsize = 15, fontweight = "bold")
axs[1][1].set_ylabel("TONS", color = "r")
axs[1][1].set_xticks(np.arange(1750, 2011, 20))
axs[1][1].set_yticks(np.arange(0, 4000, 175))
axs[1][1].grid()

axs[1][2].plot(annoCO2, gasFuel,  "go", label = "gas fuel", markersize = 0.2)
axs[1][2].plot(annoCO2, liquidFuel,  "ro", label = "liquid fuel", markersize = 0.2)
axs[1][2].plot(annoCO2, solidFuel,  "yo", label = "solid fuel", markersize = 0.5)
axs[1][2].set_title("FUELS EMISSION", color = "b", fontsize = 15, fontweight = "bold")
axs[1][2].set_ylabel("TONS", color = "r")
axs[1][2].set_xticks(np.arange(1750, 2011, 20))
axs[1][2].set_yticks(np.arange(0, 4000, 250))
axs[1][2].legend()
axs[1][2].grid()

plt.savefig("CO2_emissions.png")
plt.show()

#######################################################################

fig, ax = plt.subplots(figsize = (28, 7)) 
plt.xticks(rotation=90)
ax.plot(annoCO2, totale, "r-")
ax.set_title("Total Emissions", fontsize = 30, color = "c", fontweight = "bold")
ax.set_xlabel("YEAR", color = "r", fontweight = "bold")
ax.set_xticks(np.arange(1750, 2011, 5))
ax.set_ylabel("TONS", color = "r", fontweight = "bold")
ax.set_yticks(np.arange(0, 9201, 400))
ax.grid()

plt.savefig("TotalEmissions.png")
plt.show()


#######################################################################

fig, ax = plt.subplots(figsize = (28, 7)) 
plt.xticks(rotation=90)
ax.plot(annoCO2[198:], perCapita[198:], "y-", markersize = 0.)
ax.set_title("Per capita Emissions", fontsize = 30, color = "y", fontweight = "bold")
ax.set_xlabel("YEAR", color = "g", fontweight = "bold")
ax.set_xticks(np.arange(1949, 2011, 3))
ax.set_ylabel("TONS", color = "r", fontweight = "bold")
#ax.set_yticks([0, 0.15, 0.30, 0.45, 0.60, 0.75, 0.90, 1.05, 1.20, 1.35, 1.50])
ax.grid()

plt.savefig("PerCapitaEmissions.png")
plt.show()


##############################################################################

fig, axs = plt.subplots(nrows = 2, ncols = 1, figsize = (30, 10), layout="constrained") 
plt.suptitle("Temperature Anomaly - CO2 Emissions", fontsize = 30, color = "r", fontweight = "bold")

axs[0].bar(annoAnomalia, anomalia)
axs[0].set_xlabel("YEAR", color = "g", fontweight = "bold")
axs[0].set_xticks(np.arange(1880, 2020, 5))
axs[0].set_ylabel("GRADES [°C]", color = "r", fontweight = "bold")
axs[0].set_yticks(np.arange(-0.5, 1, 0.075))
axs[0].grid()


axs[1].plot(annoAnomalia, totale[122:], "c-")
axs[1].set_xlabel("YEAR", color = "g", fontweight = "bold")
axs[1].set_xticks(np.arange(1880, 2020, 5))
axs[1].set_ylabel("TONS", color = "r", fontweight = "bold")
axs[1].set_yticks(np.arange(0, 9201, 400))
axs[1].grid()

plt.savefig("confronto.png")
plt.show()





