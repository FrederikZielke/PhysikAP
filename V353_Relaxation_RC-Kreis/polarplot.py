import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def g(x,a):
    return(np.absolute(np.arctan(-x*a)))

v, U_C, a, b = np.genfromtxt('content/phasenMesswerte.txt', unpack=True)
U0 = 2.9

phi = 2*np.pi*(a/b)
tRange = np.linspace(np.min(v),np.max(v),1000)
params, pcov = curve_fit(g, v, phi, p0 = 2)

RC1=params[0]
RC2=params[0]

plt.clf()
x=np.linspace(0,50*v[-1],10000)
ax=plt.figure().add_subplot(111,polar=True)
ax.plot(phi, U_C/U0,"xb",label="Messwerte")
ax.plot(np.absolute(np.arctan(-x*RC1)),1/np.sqrt(1+(x*RC1)**2),"--r",label="Theorie")
ax.set_thetamax(90)
ax.legend()
#plt.show()
plt.savefig("build/plotNp.pdf")