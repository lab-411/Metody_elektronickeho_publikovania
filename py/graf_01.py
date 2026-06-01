from numpy import *
import pylab as plt
#plt.rcParams['figure.dpi'] = 150

plt.style.use("ggplot")

T = linspace(0, 5*pi*2, 1000)     # 2*pi*t

m  = 0.5
A0 = 1
ct = A0*(1 + m*cos(T))     # modulacny signal
am = ct * cos(10*T)        # amplitudova modulacia

plt.plot(T, am)
plt.plot(T, ct, 'k--')
plt.plot(T,-ct, 'k--')
plt.title(r'Modulačný činiteľ ' + str(m))
plt.grid()
plt.xlabel('t')
plt.ylabel('AM')

#plt.savefig('am_signal.png', dpi=300)
#plt.close()

import matplot2tikz
matplot2tikz.clean_figure()
matplot2tikz.save("test.tex")
