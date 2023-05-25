import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

r_innen = ufloat(10, 1)
r_aussen = ufloat(15, 1)
h = ufloat(20, 1)

v_zylinder = np.pi*h*(r_aussen**2 - r_innen**2)
print(v_zylinder)

m = ufloat(5.0, 0.1)
v = ufloat(200, 10)

s = v*6
print(s)
e_kin = 1/2*m*v**2
print(e_kin)
