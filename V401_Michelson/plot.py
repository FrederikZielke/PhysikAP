import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy as unp
from uncertainties import ufloat

r, v = np.genfromtxt('content/messung_wellenlaenge.csv', unpack = True, delimiter = ',')

#Bestimmung der Wellenlänge

motor = ufloat(5, 0.1) * 10**(-3)

delta_s1 = motor/5.056 #Teil 1 Übersetzung 1:5.056
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

#Bestimmung des Brechungsindize

i, o = np.genfromtxt('content/messung_pumpe.csv')



