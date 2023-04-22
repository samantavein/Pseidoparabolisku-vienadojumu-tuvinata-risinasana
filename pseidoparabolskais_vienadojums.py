import matplotlib.pyplot as plt
import numpy as np
import math

fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(25, 5))
#nodefinee funkciju
def y(x):
    return np.sin(np.pi*x)
intervals = 1
h=0.1
punkti = int(intervals/h + 1)
Ʈ=h
γ=Ʈ/h**2
σ = 1
l=10
η=1

fx = np.linspace(0, intervals)
fy = y(fx)
x = np.arange(0, intervals + 0.1, h)

#aprekina y vērtības
y = y(x)


print("x:", x, "y:", y )
axs[0].plot(x, y, 'ro')
axs[0].plot(fx, fy, '--')

# definee γ, h, Ʈ, kur γ=Ʈ/h**2


print("γ=",γ)
print("σ=",σ)

#izvedo nullu matricu kurā pēc tam saglabā u(xi,yi) vertibas
u = np.zeros((punkti,l))
α = np.zeros((punkti,l))
β = np.zeros((punkti,l))
z = np.zeros((l))

for i in range(0,punkti-1):
  u[i,0] = y[i]

for j in range (1,l):
  for i in range(0,punkti-2):
    A= (γ*σ + η*γ*σ)
    B= (γ*σ + η*γ*σ)
    C= (2*γ*σ + 2*γ*σ*η+1)
    F = -(((η*γ*σ)*u[i,j-1]) - ((1 + 2*γ*σ*η) * u[i+1,j-1]) + ((η*γ*σ)*u[i+2,j-1]))

    α[i+1,j] = B/(C-A*α[i,j])
    β[i+1,j] = (A*β[i,j]+F)/(C-A*α[i,j])

  for i in range(punkti-2,0,-1):
    u[i,j] = α[i,j]*u[i+1,j]+β[i,j]

print("α:",α[:])
print("β:", β[:])
print(u[:,:])

# konstruē grafikus
for i in range(0,l):
  axs[1].plot(u[:,i], 'bo')
  axs[1].plot(u[:,i], 'b--')

for i in range(0,l):
  print("u(",i,")", u[:,i])
  z[i]= u[2,i]
 
axs[2].plot(z[:], 'bo')
axs[2].plot(z[:], 'b--')