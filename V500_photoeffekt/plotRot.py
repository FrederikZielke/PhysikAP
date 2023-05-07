import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy as unp
from uncertainties import ufloat
from scipy.stats import linregress

U_rot, I_rot = np.genfromtxt('content/messung_rot.csv', unpack = True, delimiter = ',')


I_rot = np.sqrt(I_rot)

start = 0
stop = 0
for i in range(I_rot.size):
    if I_rot[i] > 0:
        if start == 0:
            start = i -  1
    if I_rot[i] > 0.13:
        stop = i
        print(I_rot[i])
        break

lin_rot = linregress(U_rot[start:stop], I_rot[start:stop])
a1_rot = ufloat(lin_rot.slope, lin_rot.stderr)
b1_rot = ufloat(lin_rot.intercept, lin_rot.intercept_stderr)
a_rot = lin_rot.slope
b_rot = lin_rot.intercept
U_g_rot = -b_rot/a_rot
x_rot = np.linspace(U_g_rot, U_rot[stop])
print(f'U_g_rot liegt bei {U_g_rot}V')

plt.plot(U_rot, I_rot, 'rx', label = r'Messwerte')
plt.plot(x_rot, (a_rot*x_rot+b_rot), color = 'black', label = r'Ausgleichsgerade')
plt.xlabel(r'$U \:/\: [V]$')
plt.ylabel(r'$\sqrt{I} \:/\: [\sqrt{nA}]$')
plt.title('Rotes Licht')
plt.legend(loc='best')
plt.minorticks_on()
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

#plt.show()
plt.savefig('build/plotRot.pdf')