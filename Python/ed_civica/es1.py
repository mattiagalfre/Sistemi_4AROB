import matplotlib.pyplot as plt

X = [x for x in range(10)]
y = [x**2 for x in X]

fig, ax = plt.subplots(figsize = (8, 8))        #fig = finestra sullo schermo, ax = assi
ax.plot(X, y, 'gs--')
ax.set_title("Primo grafico", fontsize = 30)
ax.set_xlabel("Etichetta asse x (unità di misura)")
ax.set_ylabel("Etichetta asse y (unità di misura)")
ax.grid()
plt.show()

