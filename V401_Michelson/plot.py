import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy as unp
from uncertainties import ufloat

r, v = np.genfromtxt('content/messung_wellenlaenge.csv', unpack = True, delimiter = ',')

#Bestimmung der Wellenlänge

motor = ufloat(5, 0.1) * 10**(-3)

delta_s1 = motor/5.046 #Teil 1 Übersetzung 1:5.046
delta_s2 = motor/5.017 #Teil 2 Übersetzung 1:5.017
#Mittelwert rückwärts
r_mean = 0
for i in range(len(r)):
    r_mean = r_mean + r[i]
r_mean = r_mean/len(r)

#Mittelwert rückwärts
v_mean = 0
for i in range(len(v)):
    v_mean = v_mean + v[i]
v_mean = v_mean/len(v)

r_miterr = ufloat(r_mean, 100)
v_miterr = ufloat(v_mean, 50)

lambda_r = (2*delta_s1)/r_mean
lambda_v = (2*delta_s1)/v_mean

#print(lambda_r, lambda_v)
#Bestimmung des Brechungsindize

i, o = np.genfromtxt('content/messung_brechungsindex.csv', unpack = True, delimiter = ',')

o = o-i

i_mean = 0
for s in range(len(o)):
    i_mean = i_mean + i[s]
i_mean = i_mean/len(o)

o_mean = 0
for i in range(len(o)):
    o_mean = o_mean + o[i]
o_mean = o_mean/len(o)

delta_p = ufloat(600, 20)*133.322
p_0 = 101325
T_0 = 273.15
T = ufloat(293.15, 1)
b = 50 * 10**(-3)
lam = 680 * 10**(-9)

in_mean = ufloat(i_mean, 3)
out_mean = ufloat(o_mean, 3)
mean = (in_mean + out_mean)/2

delta_n = (mean*lam*T*p_0)/(2*b*T_0*delta_p)
n = delta_n + 1
print(n)
#print(r_mean, v_mean)


