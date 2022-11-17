import numpy as np
import matplotlib.pyplot as plt
v = np.zeros (180) # esse v aqui é só pra saber o valor real, n serve para nada por enquanto
tempt = np.zeros (180)
tempo = np.linspace (0, 180, 180)
kcres = np.linspace (293, 333, 60)
kdecres = np.linspace (333, 273, 60)
for i in range (1, 181, 1):
    if i <= 60:
        v[i-1] = 0.3*8*kcres[i-1]
        tempt[i-1] = kcres[i-1] - 273
    elif i > 60 and i <= 90:
        v[i-1] = 0.3*8*333
        tempt[i - 1] = 333 - 273
    elif i > 90 and i <= 150:
        v[i-1] = (0.3*8*kdecres[i-91])
        tempt[i-1] = kdecres[i-91] - 273
    else:
        v[i-1] = 0.3*8*273 
        tempt[i-1] = 273 - 273      
fig, ax = plt.subplots(figsize=(3,2), constrained_layout=True)
ax.plot(tempo, tempt)
ax.set_xlabel('tempo [min]')
ax.set_ylabel('temperatura [ºC]')
ax.set_title('Gráfico >:(')
fig.set_facecolor('red')
plt.show()
input()