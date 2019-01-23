# to simplify plotting 
import sys
import matplotlib.pyplot as plt

def assertfloat(l):
	return list(map(lambda z : float(z), l))

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

with open("data.txt", 'r') as f:
	line = f.readline()
	t = line.split(' ')[:-1]
	line = f.readline()
	f_t = line.split(' ')[:-1]
	line = f.readline()
	freq = line.split(' ')[:-1]
	line = f.readline()
	mag = line.split(' ')[:-1]

# assert types
t = assertfloat(t)
f_t = assertfloat(f_t)
mag = assertfloat(mag)

# plot input signal samples	
ax1.set_xlabel("t")
ax1.set_ylabel("x(t)")
ax1.set_title("Input function")
ax1.scatter(t, f_t, color='g')
ax1.plot(t,f_t, '--o')

ax2.set_xlabel("sampling frequency Hz")
ax2.set_ylabel("magnitude")
ax2.set_title("FFT(x(t))")
ax2.bar(freq, mag, color='g')

plt.show()

