import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(3*-np.pi, 3*np.pi, 256, endpoint=True)
plt.figure(figsize=(15,5))
C,S = np.cos(X), np.sin(X)

plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cos(x)")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sin(x)")

plt.xticks( [-3*np.pi, -5/2*np.pi, -2*np.pi, -3/2*np.pi, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3/2*np.pi, 2*np.pi, 5/2*np.pi, 3*np.pi],
            [r'$-3\pi$', r'$-5\pi/2$', r'$-2\pi$', r'$-3\pi/2$', r'$-\pi$',
             r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$',
             r'$3\pi/2$', r'$2\pi$', r'$5\pi/2$', r'$3\pi$'])

plt.legend(loc='upper left', frameon=False)

plt.show()