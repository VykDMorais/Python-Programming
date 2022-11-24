import numpy as np
import matplotlib.pyplot as plt
plt.close ('all')
time = np.arange (0, 180.5, 0.5)
tam = len (time)
Tempt = np.empty(tam)
Tempt.fill (np.NAN)
for i in range (tam):
    if time [i] <= 60:
        Tempt[i] = (2/3)*time[i] + 20
    elif time[i] > 60 and time[i] <= 90:
        Tempt [i] = 60
    elif time [i] > 90 and time[i] <= 150:
        Tempt[i] = -(time[i]-90)+60
    else:
        Tempt[i] = 0
plt.figure ()
plt.plot(time, Tempt)
'''
plt.plot (time [0:120], Tempt[0: 120], 'b')
plt.plot (time [121:180], Tempt[0: 180], 'r')
'''
plt.grid ()
plt.xlabel ('tempo [min]')
plt.ylabel ('T(ºC)')
plt.xlim ((0, 180))
plt.ylim ((0, 80))
v  = 0.3*8.31*(Tempt+273)
plt.figure ()
plt.plot(Tempt, v)
plt.xlabel ('T(ºC)')
plt.ylabel ('V(L)')
plt.figure()
plt.plot (time, v)
plt.xlabel ('Tempo(min)')
plt.ylabel ('V(L)')
plt.figure ()
plt.subplot(2, 1, 1)
plt.plot(time, Tempt, 'c')
plt.grid()
plt.xlabel ('T(ºC)')
plt.xlim ((0, 180))
plt.subplot(2, 1, 2)
plt.plot(time, v, 'b')
plt.grid()
plt.ylabel ('V(L)')
plt.xlabel ('tempo(min)')
plt.xlim ((0, 180))
input()