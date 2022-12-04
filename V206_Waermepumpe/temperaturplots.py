import matplotlib.pyplot as plt
import numpy as np

t, T2, T1, pa, pb, N, = np.genfromtxt('content/messwerte.txt', unpack = True)


#plt.subplots(constrained_layout = True)

#plt.subplot(2, 2, 1)
plt.plot(t, T1, 'gx', label = r'Messwerte $T_1$')
plt.plot(t, T2, 'rx', label = r'Messwerte $T_2$')
plt.legend(loc="best")
plt.xlabel(r'$t \,[$s$]$')
plt.ylabel(r'$T \,[°$C$]$')
plt.title(r"Temperaturen")

#plt.subplot(2, 2, 2)
#plt.plot(t, pa, '.b', label = r'$p_a$')
#plt.plot(t, pb, '.r', label = r'$p_b$')
#plt.legend(loc="best")
#plt.xlabel(r'$t \,[$s$]$')
#plt.ylabel(r"$p \,[$bar$]$")
#plt.title(r'Druck')

#plt.subplot(2, 2, 3)
#plt.plot(T1, pa, '*', label = r'Kalt')
#plt.plot(T2, pb, 'h', label = r'Warm')
#plt.legend(loc="best")
#plt.xlabel(r'$T \,[°$C$]$')
#plt.ylabel(r"$p \,[$bar$]$")
#plt.title(r'p/T')

#Plot Druck pro 1/T
#T2 = 1/T2


#plt.subplot(2, 2, 4)
#plt.plot(T2, pb, '.', label=r"\frac{1}{T_{1}}(pa)")

plt.savefig('build/temperaturplots.pdf')
#plt.show()