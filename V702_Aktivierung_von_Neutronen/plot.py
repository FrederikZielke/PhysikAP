import matplotlib.pyplot as plt
import numpy as np

n = np.genfromtxt('content/silber2.csv', delimiter = ',', unpack = True)

t = np.linspace(10, 430, 43)

plt.plot(t, n, 'bx')

plt.legend(loc='best')
plt.yscale('log')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.show()
plt.savefig('build/plot2.pdf')
