import numpy as np
import matplotlib.pyplot as plt
pi=3.141592653
x=np.linspace(-49,49,99)
y=np.sin(2*pi*x/49)+np.sin(25*pi*x/49)
ffty=np.fft.fft(y)
plt.plot(np.abs(ffty))
plt.show()
