import matplotlib.pyplot as plt
import numpy as np

d, N = np.genfromtxt("data.txt", unpack=True)

plt.figure(constrained_layout=True)


fig1 = plt.subplot(1, 2, 1)
plt.plot(d, N, ".")
plt.xlabel(r"d [cm]")
plt.ylabel(r"N [1/60s]")
fig1.set_title(r'lineare Darstellung')


fig2 = plt.subplot(1, 2, 2)
plt.plot(d, N, ".")
plt.xlabel(r"d [cm]")
plt.ylabel(r"N [1/60s]")
plt.yscale("log")
fig2.set_title(r'halblogarithmische Darstellung')

# in matplotlibrc leider (noch) nicht möglich
#plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
