import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy as unp


m_halter = ufloat(50.1, 0.1)
m_500 = ufloat(499.4, 0.1)
m_1000 = ufloat(1001.9, 0.1)
m_halter, m_500, m_1000 = m_halter/1000, m_500/1000, m_1000/1000

d_e = ufloat(1, 0.005)
l_e = ufloat(60, 0.1)
m_e = ufloat(502.5, 0.1)
d_e /= 100
l_e /= 100
m_e /= 1000

d_r = ufloat(1, 0.005)
l_r = ufloat(59.1, 0.1)
m_r = ufloat(390.1, 0.1)
d_r /= 100
l_r /= 100
m_r /= 1000
r_r = d_r/2

I_e = (1/12)*(d_e**4)
I_r = (1/4)*np.pi*(r_r**4)

print(r'Flächenträgheitsmoment des eckigen Stabs: I_e =', I_e)
print(r'Flächenträgheitsmoment des runden Stabs: I_r =', I_r)