import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

rpm15, f_mean15, f_max15 = np.genfromtxt("content/messung15.txt", unpack = True)
rpm30, f_mean30, f_max30 = np.genfromtxt("content/messung30.txt", unpack = True)
rpm45, f_mean45, f_max45 = np.genfromtxt("content/messung45.txt", unpack = True)

#Konstanten
c_fl = 1800
c_pr = 2700
f_0 = 2*10**(6)
#Winkel
a = [np.radians(80.6), np.radians(70.5), np.radians(54.7)]

#Arrays sind toll
rpm = [rpm15, rpm30, rpm45]
f_mean = [f_mean15, f_mean30, f_mean45]
f_max = [f_max15, f_max30, f_max45]
fdiff = [0, 0, 0]
nice = ["15: ", "30: ", "45: "]

#Frequenzverschiebung
for i in range(len(f_mean)):
    fdiff[i] = np.abs(f_mean[i] - f_max[i])
    print(nice[i] ,fdiff[i])

v = [0, 0, 0]
#Geschwindigkeit 
for i in range(len(f_mean)):
    v[i] = (fdiff[i] * c_fl)/(2*f_0*np.cos(a[i]))
    print(nice[i], v[i])

plot_y = [0, 0, 0]
for i in range(len(v)):
    plot_y[i] = fdiff[i]/np.cos(a[i])
    print(nice[i], plot_y[i])

plt.plot(v[0], plot_y[0], 'bx', label = 'Messwerte bei 15°')
plt.xlabel(r'$v \,$[m/s]')
plt.ylabel(r'$ \frac{\Delta f}{cos(\alpha)} \,$[Hz]')
plt.grid()
plt.legend()
plt.savefig('build/15.pdf')
plt.clf()

plt.plot(v[1], plot_y[1], 'bx', label = 'Messwerte bei 30°')
plt.xlabel(r'$v \,$[m/s]')
plt.ylabel(r'$ \frac{\Delta f}{cos(\alpha)} \,$[Hz]')
plt.grid()
plt.legend()
plt.savefig('build/30.pdf')
plt.clf()

plt.plot(v[2], plot_y[2], 'bx', label = 'Messwerte bei 45°')
plt.xlabel(r'$v \,$[m/s]')
plt.ylabel(r'$ \frac{\Delta f}{cos(\alpha)} \,$[Hz]')
plt.grid()
plt.legend()
plt.savefig('build/45.pdf')


