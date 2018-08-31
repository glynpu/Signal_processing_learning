import numpy as np
import matplotlib.pyplot as plt
A=4
fc=40
fs=20*fc
pi=3.141592653


fft_length=80*fc
x=np.linspace(0,2*fs-1,2*fs)/fs
y=A*np.sin(fc*2*pi*x)
df=fs*1.0/fft_length
#feque=np.linspace(0,df*fft_length-df,fft_length)
feque=np.linspace(0,fft_length-1,fft_length)
#print(feque)

plt.subplot(3,2,1)
plt.plot(x,y)

cy=y[:fft_length]
conyy=np.convolve(cy,cy)
fconyy=np.fft.fft(conyy,fft_length)/(fft_length*fft_length)
plt.subplot(3,2,3)
plt.plot(np.abs(conyy))
plt.subplot(3,2,5)
plt.plot(feque,np.abs(fconyy))

ffty=np.fft.fft(y,fft_length)
plt.subplot(3,2,2)
print(df)
plt.text(np.argmax(np.abs(ffty)),0.5,np.argmax(np.abs(ffty))*df)
plt.plot(feque,np.abs(ffty)/fft_length,np.argmax(np.abs(ffty)),np.max(np.abs(ffty)/fft_length),'bs')
plt.subplot(3,2,4)
plt.plot(feque,np.abs(ffty*ffty)/(fft_length*fft_length))
plt.subplot(3,2,6)
plt.plot(np.abs(np.fft.ifft(ffty*ffty)))

plt.show()
