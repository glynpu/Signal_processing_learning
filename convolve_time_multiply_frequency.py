import numpy as np

a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
print("should set fft lenght or will wrong")
x=np.fft.fft(a)
y=np.fft.fft(b)
print(np.abs(np.fft.ifft(x*y)))
print(np.convolve(a,b))
print("set fft lenght as n1+n2-1")
x1=np.fft.fft(a,9)
y1=np.fft.fft(b,9)
print("inverse of multiplication of frequency domain")
print(np.abs(np.fft.ifft(x1*y1)))
print(np.convolve(a,b))

print("fft of convolution of time domain")
print(np.fft.fft(np.convolve(a,b),9))
print(x1*y1)
