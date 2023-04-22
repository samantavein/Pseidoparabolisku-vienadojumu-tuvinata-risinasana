import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(25, 5))
# define function
def y(x):
    return -x**2 + 4*x

# plot function in the interval x[-1;5]
fx = np.linspace(-1, 5)
fy = y(fx)

x = np.arange(-1, 5.1, 1)
# calculate y values
y = y(x)

print("x:", x, "y:", y)
axs[0].plot(x, y, 'ro')
axs[0].plot(fx, fy, '--')

# define γ, h, Ʈ, where γ=Ʈ/h**2
h = 5
Ʈ = h
γ = Ʈ / (h**2)
n=50
print("γ=",γ)

# create a matrix of zeros to store u(xi,yi) values
u = np.zeros((6,n))
z = np.zeros((n))

for i in range(-1,5):
  u[i,0] = y[i+1]

for j in range(1,n):
    for i in range(0,5):
        u[i,j] = γ * (u[i+1,j-1] - 2 * u[i,j-1] + u[i-1,j-1]) + u[i,j-1]

for i in range(n):
    u[0,i] = 0
    u[4,i] = 0
    axs[1].plot(u[:5,i], 'bo')
    axs[1].plot(u[:5,i], 'b--')

for i in range(n):
  u[0,i] =0
  u[4,i] =0
  print("u(",i,")", u[:5,i])
  z[i]= u[2,i]
axs[2].plot(z[:], 'bo')
axs[2].plot(z[:], 'b--')
