import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unumpy
from scipy.optimize import curve_fit

#Ausgleichsfunktion
def f(x, A, B, D):
    return (A / (1 + B * (x ** D)))

def g(x, A, B, C):
    return A*x**2 + B*x + C

#Messdaten
t, T1, T2, pa, pb, N, = np.genfromtxt('messwerte.txt', unpack = True)

#Subplot und Curvefit T1
params1, covariance_matrix1 = curve_fit(g , t, T1, p0=(10,100,10))


uncertainties1 = np.sqrt(np.diag(covariance_matrix1))

#plt.subplot(1, 2, 1)
plt.plot(t, g(t, *params1), 'g-')
plt.plot(t, T1, 'gx', label = r'Gekühltes Becken')

#Subplot und Curvefit T2
params2, covariance_matrix2 = curve_fit(g , t, T2, p0=(10,100,10))


uncertainties2 = np.sqrt(np.diag(covariance_matrix1))


#plt.subplot(1, 2, 2)
plt.plot(t, g(t, *params2), 'b-')
plt.plot(t, T2, 'bx', label = r'Erwärmtes Becken')

plt.xlim(np.min(t), np.max(t))

plt.legend(loc="best")
plt.show()

print('Parameter T1')
#for name, value, uncertainty in zip('abc', params1, uncertainties1): 
#    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')
print(*params1)

print('Parameter T2')
#for name, value, uncertainty in zip('abc', params2, uncertainties2): 
#   print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')
print(*params2)