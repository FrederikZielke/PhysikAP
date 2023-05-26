import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

#3870rpm
s1, v1, I1 = np.genfromtxt("content/messung3870.txt", unpack = True)

#6020rpm
s2, v2, I2 = np.genfromtxt("content/messung6020.txt", unpack = True)

#Umrechnung in SI
s1 = s1*10**(-6)
s2 = s2*10**(-6)
v1 = v1/100
v2 = v2/100

#Plot s gegen v
plt.plot(s1, v1, 'bx', label = 'Messwerte bei 3870rpm')
plt.plot(s2, v2, 'rx', label = 'Messwerte bei 6020rpm')
plt.ylabel(r'$v \,$[m/s]')
plt.xlabel(r'$s$[m]')
plt.grid()
plt.legend()
plt.savefig('build/s_gegen_v.pdf')
plt.clf()

#Plot s gegen I
plt.plot(s1, I1, 'bx', label = 'Messwerte bei 3870rpm')
plt.plot(s2, I2, 'rx', label = 'Messwerte bei 6020rpm')
plt.ylabel(r'$I \:[1000V^2/s]$')
plt.xlabel(r'$s$[m]')
plt.grid()
plt.legend()
plt.savefig('build/s_gegen_I.pdf')
plt.show()
