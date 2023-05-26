import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy as unp
from uncertainties import ufloat
from scipy.stats import linregress

#def plot(x, y, color):
#    fig, ax = plt.subplots(2,2, constrained_layout=True)
#    fig.subtitle(f'Messung bei {color} Licht')
#    for j in range(len(ax)):
#        for i in range(len(ax[0])):
#            ax[j][i].plot()

U_lila, I_lila = np.genfromtxt('content/messung_lila.csv', unpack = True, delimiter = ',')
U_gelb, I_gelb = np.genfromtxt('content/messung_gelb.csv', unpack = True, delimiter = ',')
U_gruen, I_gruen = np.genfromtxt('content/messung_gruen.csv', unpack = True, delimiter = ',')
U_rot, I_rot = np.genfromtxt('content/messung_rot.csv', unpack = True, delimiter = ',')

I_lila = I_lila * 10**(-9)  
I_gelb = I_gelb * 10**(-9)
I_gruen = I_gruen * 10**(-9)
I_rot = I_rot * 10**(-9)



I_lila = np.sqrt(I_lila)
I_gelb = np.sqrt(I_gelb)
I_gruen = np.sqrt(I_gruen)
I_rot = np.sqrt(I_rot)

#params, covariance_matrix = np.polyfit(U_lila, I_lila, deg=1, cov=True)
#errors = np.sqrt(np.diag(covariance_matrix))
#x_plot_lila = np.linspace(-2,2)
start = 0
stop = 0
#for i in range(I_lila.size):
#    if I_lila[i] > 0:
#        if start == 0:
#            start = i
#    if I_lila[i] > 1:
#        stop = i
#        print(I_lila[i])
#        break
#



#lin_lila = linregress(U_lila[start-1:stop], I_lila[start-1:stop])
#a1_lila = ufloat(lin_lila.slope, lin_lila.stderr)
#b1_lila = ufloat(lin_lila.intercept, lin_lila.intercept_stderr)
#a_lila = lin_lila.slope
#b_lila = lin_lila.intercept
#x_lila = np.linspace(U_lila[start - 5], U_lila[stop])


plt.subplots(2,2, constrained_layout=True)


plt.subplot(2,2,1)
plt.plot(U_lila, I_lila, 'mx', label = r'Messwerte')
#plt.plot(x_lila, (a_lila*x_lila+b_lila), color = 'black', label = r'Ausgleichsgerade')
#plt.plot(x_plot_lila, params[0]*x_plot_lila + params[1], 'k-', label='Lineare Regression')
plt.xlabel(r'$U \:/\: [V]$')
plt.ylabel(r'$\sqrt{I} \:/\: [\sqrt{nA}]$')
plt.title('Lilanes Licht')
plt.legend(loc='best')
plt.minorticks_on()
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')

plt.subplot(2,2,2)
plt.plot(U_gelb, I_gelb, 'yx')
plt.xlabel(r'$U \:/\: [V]$')
plt.ylabel(r'$\sqrt{I} \:/\: [\sqrt{nA}]$')
plt.title('Gelbes Licht')
plt.minorticks_on()
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')

plt.subplot(2,2,3)
plt.plot(U_gruen, I_gruen, 'gx')
plt.xlabel(r'$U \:/\: [V]$')
plt.ylabel(r'$\sqrt{I} \:/\: [\sqrt{nA}]$')
plt.title('Grünes Licht')
plt.minorticks_on()
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')


plt.subplot(2,2,4)
plt.plot(U_rot, I_rot, 'rx')
plt.xlabel(r'$U \:/\: [V]$')
plt.ylabel(r'$\sqrt{I} \:/\: [\sqrt{nA}]$')
plt.title('Rotes Licht')
plt.minorticks_on()
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

plt.show()

#plt.plot(U, I, 'k.', label = r'Messwerte')
#plt.xlabel(r'$U \:/\: [V]$')
#plt.ylabel(r'$\sqrt{I} \:/\: [\sqrt{A}]$')
#plt.legend(loc='best')
#plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
#plt.savefig('build/plot_lila.pdf')
#plt.show()
#plt.clf()