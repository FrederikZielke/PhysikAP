import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as sc
from uncertainties import unumpy as unp
from uncertainties import ufloat

E_abs = 8.9789 * 10**3 #Absorption Edge Copper
E_a_theorie = 8.048 * 10**3
E_b_theorie = 8.907 * 10**3
TZ = 29 #Kupfer
R = 13.6
d = 2.014 * 10**(-10)
n = 1
t_b = np.radians(20.2)
t_a = np.radians(22.5)
th_b1 = np.radians(40.8/2)
th_b2 = np.radians(39.9/2)
th_a1 = np.radians(45.5/2)
th_a2 = np.radians(44.5/2)
t_b_err = np.radians(0.1)
t_a_err = np.radians(0.1)
th_b1_err = np.radians(0.1)
th_b2_err = np.radians(0.1)
th_a1_err = np.radians(0.1)
th_a2_err = np.radians(0.1)
t_b_mitfehler = ufloat(t_b, t_b_err)
t_a_mitfehler = ufloat(t_a, t_a_err)
th_b1_mitfehler = ufloat(th_b1, th_b1_err)
th_b2_mitfehler = ufloat(th_b2, th_b2_err)
th_a1_mitfehler = ufloat(th_a1, th_a1_err)
th_a2_mitfehler = ufloat(th_a2, th_a2_err)
#Absorption
t_zn = np.radians(40.1/2)
t_br = np.radians(26.4/2)
t_zr = np.radians(20/2)
t_sr = np.radians(22.1/2)
t_zn_err = np.radians(0.1)
t_br_err = np.radians(0.1)
t_zr_err = np.radians(0.1)
t_sr_err = np.radians(0.1)
t = [t_zn, t_br, t_zr, t_sr]
t_err = [t_zn_err, t_br_err, t_zr_err, t_sr_err]
t_mitfehler = unp.uarray(t, t_err)
#minimale Wellenlänge
l_a = (2*d*unp.sin(t_a_mitfehler))/(n)
l_b = (2*d*unp.sin(t_b_mitfehler))/(n)
lh_a1 = (2*d*unp.sin(th_b1_mitfehler))/(n)
lh_a2 = (2*d*unp.sin(th_b2_mitfehler))/(n)
lh_b1 = (2*d*unp.sin(th_a1_mitfehler))/(n)
lh_b2 = (2*d*unp.sin(th_a2_mitfehler))/(n)
#Absorption Energie
l = [0, 0, 0, 0]
E = []
Kom = ["Zn: ", "Br: ", "Zr: ", "Sr: "]
for i in range (len(l)):
    l[i] = (2*d*unp.sin(t_mitfehler[i]))/(n)
    E.append((sc.h*sc.c)/(l[i])*6.242*10**(18))
    print(Kom[i], E[i])
#Absorption Abschirmung
sig = []
Z = [30, 35, 40, 38]
print("Abschirmung")
for i in range(len(E)):
    sig.append(Z[i] - unp.sqrt(E[i]/R))
    print(Kom[i], sig[i])
#Energie
E_a = (sc.h*sc.c)/(l_a)
E_b = (sc.h*sc.c)/(l_b)
Eh_a1 = (sc.h*sc.c)/(lh_a1)
Eh_a2 = (sc.h*sc.c)/(lh_a2)
Eh_b1 = (sc.h*sc.c)/(lh_b1)
Eh_b2 = (sc.h*sc.c)/(lh_b2)
#Umrechnung in eV
E_a = E_a * 6.242*10**(18)
E_b = E_b * 6.242*10**(18)
Eh_a1 = Eh_a1 * 6.242*10**(18)
Eh_a2 = Eh_a2 * 6.242*10**(18)
Eh_b1 = Eh_b1 * 6.242*10**(18)
Eh_b2 = Eh_b2 * 6.242*10**(18)

#Differenz E-Halbwertszeit
Eh_a = Eh_a2 - Eh_a1
Eh_b = Eh_b2 - Eh_b1

#Auflösungsvermögen
A_a = E_a / Eh_a
A_b = E_b / Eh_b

#Abschirmkonstanten
Tsig1 = TZ - unp.sqrt(E_abs/R)
Tsig2 = TZ - 2 * unp.sqrt((E_abs/R) - (E_a/R))
Tsig3 = TZ - 3 * unp.sqrt((E_abs/R) - (E_b/R))

print("Wellenlänge K_a: ", l_a)
print("Wellenlänge K_b: ", l_b)
print("Energie K_a: ", E_a)
print("Energie K_b: ", E_b)
print("Energie Halbwertsbreite K_a: ", Eh_a)
print("Energie Halbwertsbreite K_b: ", Eh_b)
print("Auflösungsv. K_a: ", A_a)
print("Auflösungsv. K_b: ", A_b)
print("Sigma 1: ", Tsig1)
print("Sigma 2: ", Tsig2)
print("Sigma 3: ", Tsig3)