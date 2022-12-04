import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unumpy

#Messdaten
t, T1, T2, pa, pb, N, = np.genfromtxt('messwerte.txt', unpack = True)

##5c alles quatsch was ich gemacht habe
#
#dT1 = np.diff(T1) * (1/60)
#dT2 = np.diff(T2) * (1/60)
#
##Temperaturdifferentialquotienten dT1/dt
#print("dT1/dt")
#for i in range(1, 5):
#    print(dT1[5*i - 1])
#
##Temperaturdifferentialquotienten dT2/dt
#print("dT2/dt:")
#for j in range(1,5):
#    print(dT2[5*j -1])

#5d
