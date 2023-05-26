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
t, T2, T1, pa, pb, N, = np.genfromtxt('content/messwerte.txt', unpack = True)

#Subplot und Curvefit T1
params1, covariance_matrix1 = curve_fit(g , t, T1, p0=(10,100,10))


uncertainties1 = np.sqrt(np.diag(covariance_matrix1))

#plt.subplot(1, 2, 1)
plt.plot(t, g(t, *params1), 'g-')
plt.plot(t, T1, 'gx', label = r'Erwärmtes Becken')

#Subplot und Curvefit T2
params2, covariance_matrix2 = curve_fit(g , t, T2, p0=(10,100,10))


uncertainties2 = np.sqrt(np.diag(covariance_matrix2))


#plt.subplot(1, 2, 2)
plt.grid()
plt.plot(t, g(t, *params2), 'b-')
plt.plot(t, T2, 'bx', label = r'Gekühltes Becken')

plt.xlim(np.min(t), np.max(t))

plt.legend(loc="best")
plt.savefig('build/ausgleichsplot.pdf')

print("parameter 1")
print(params1)
print("unsicherheiten 1")
print(uncertainties1)
print("parameter 2")
print(params2)
print("unsicherheiten 2")
print(uncertainties2)

#print('Parameter T1')
#for name, value, uncertainty in zip('abc', params1, uncertainties1): 
#    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')
#
#print('Parameter T2')
#for name, value, uncertainty in zip('abc', params2, uncertainties2): 
#    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

A_T1 = ufloat(params1[0], uncertainties1[0])
B_T1 = ufloat(params1[1], uncertainties1[1])
C_T1 = ufloat(params1[2], uncertainties1[2])
A_T2 = ufloat(params2[0], uncertainties2[0])
B_T2 = ufloat(params2[1], uncertainties2[1])
C_T2 = ufloat(params2[2], uncertainties2[2])
m_1 = m_2 = 3
mc_k = 750
c_w = 4200

delT1_1 = 2*A_T1*240 + B_T1
delT1_2 = 2*A_T1*540 + B_T1
delT1_3 = 2*A_T1*840 + B_T1
delT1_4 = 2*A_T1*1140 + B_T1

delT2_1 = 2*A_T2*240 + B_T2
delT2_2 = 2*A_T2*540 + B_T2
delT2_3 = 2*A_T2*840 + B_T2
delT2_4 = 2*A_T2*1140 + B_T2

delT1 = [delT1_1, delT1_2, delT1_3, delT1_4]
delT2 = [delT2_1, delT2_2, delT2_3, delT2_4]

T2 = [20.1+273.15, 10.1+273.15, 3.5+273.15, 0.7+273.15]
T1 = [25.3+273.15, 34.2+273.15, 41.9+273.15, 48.2+273.15]

print(delT1_1)
print(delT1_2)
print(delT1_3)
print(delT1_4)

print(delT2_1)
print(delT2_2)
print(delT2_3)
print(delT2_4)

v_real = [0, 0, 0, 0]
N = [195, 207, 213, 205]

print("reale Gueteziffer")
for i in range (0, 4, 1):
    v_real[i] = 1/N[i] * (m_1 * c_w + mc_k) * delT1[i]
    print(v_real[i])

v_ideal = [0, 0, 0, 0]

print("ideale Gueteziffer:")
for i in range (0, 4, 1):
    v_ideal[i] = (T1[i])/(T1[i] - T2[i])
    print(v_ideal[i])

m_durchsatz = [0, 0, 0, 0]
m = ufloat(-2194.104, 45.174)
R = 8.314
L = -(m*R)/(120.913)
#molare Masse 120.913 F2Cl2C
print("L:", L)

print("Massendurchsatz")
for i in range (0, 4, 1):
    m_durchsatz[i] = (m_2 * c_w + mc_k)*(delT2[i])/(L)
    print(m_durchsatz[i])

N_mech = [0, 0, 0, 0]
k = 1.14
roh_0 = 5.51
p = 1
p_0 = 1
T_0 = 273.15


p_a = [2, 2.2, 2.2, 2.2]
p_b = [7, 9, 10.7, 12.1]

roh = [0, 0, 0, 0]

print("roh")
for i in range (0, 4, 1):
    roh[i] = (p_b[i] * roh_0 * T_0) / (p_0 * T1[i])
    print(roh[i])


print("mechanische Leistung")
for i in range (0, 4, 1):
    N_mech[i] = 1/(k-1) * (p_b[i] * (p_a[i]/p_b[i])**(1/k) - p_a[i]) * 1/roh[i] * m_durchsatz[i] * 10**2
    print(N_mech[i])


