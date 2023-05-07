import matplotlib.pyplot as plt
import numpy as np
import math
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(25, 5))

#nodefinē funkciju
def y(x):
  return np.sin(np.pi*x)

#--------------------------------------------------------------------------------------
#MAINIIGIE
# funkcijas intervaals uz x ass
intervals = 1
# sadalījums uz x ass
Nx = 100
# sadaliijums uz t ass
Nt = 100

σ = 1
η=1

# cikla izpildes reizu skaits
l=Nt+1
# apreekina sadaliijuma soli uz x ass
h = intervals/Nx
#apreekina cik punktos tiek sadaliita x ass
punkti = int(intervals/h + 1)

Ʈ=h
γ=Ʈ/h**2

#--------------------------------------------------------------------------------------
# intervaals grafika atteelosanai
fx = np.linspace(0, intervals)
fy = y(fx)
# sadala x veertiibas atkariibaa no intervaala un sadaiijuma sola h
x = np.arange(0, intervals + h, h)
#aprekina funkcijas vērtības
y = y(x)

#izprintee ieguutas x, y veertiibas, uzzkonstruee funkcijas grafiku ar preciizajaam veertiibaam
print("x:", x, "y:", y )
axs[0].plot(x, y, 'ro')
axs[0].plot(fx, fy, '--')
print("γ=",γ)
print("σ=",σ)

#-------------------------------------------------------------------------------------
#IZVEIDO NULLU MATRICAS
# u matricaa saglabaa apreekinaataas tuvinaatas vertiibas
u = np.zeros((punkti,l))
alpha = np.zeros((punkti,l))
beta = np.zeros((punkti,l))
videja_vertiba = np.zeros((l))

# saglabaa u matricaa funkcijas preciizaas veertiibas
for i in range(0,punkti-1):
  u[i,0] = y[i]

#-------------------------------------------------------------------------------------
#Tuvinato veertiibu apreekinaasana
for j in range (1,l):
  # reekina alpha un beta
  for i in range(0,punkti-2):
    A= (γ*σ + η*γ*σ)
    B= (γ*σ + η*γ*σ)
    C= (2*γ*σ + 2*γ*σ*η+1)
    F = -(((η*γ*σ)*u[i,j-1]) - ((1 + 2*γ*σ*η) * u[i+1,j-1]) + ((η*γ*σ)*u[i+2,j-1]))

    alpha[i+1,j] = B/(C-A*alpha[i,j])
    beta[i+1,j] = (A*beta[i,j]+F)/(C-A*alpha[i,j])

  #reekina tuvinaataas veertiibas
  for i in range(punkti-2,0,-1):
    u[i,j] = alpha[i,j]*u[i+1,j]+beta[i,j]

#-------------------------------------------------------------------------------------
# KONSTRUEE GRAFIKUS
# funkcijas preciizais grafiks
axs[1].plot(u[:,0], 'ro')
axs[1].plot(u[:,0], 'r--')

#funkcijas grafiki ar apreekinaatajaam tuvinaatajaam vertiibaam
for i in range(1,l):
  axs[1].plot(u[:,i], 'bo')
  axs[1].plot(u[:,i], 'b--')
#izvada katru desmito veertiibu
print("u(0)", u[::int(Nx/10),0])
print("u(1)", u[::int(Nx/10),1])


#grafiks ar funcijas videejaam vertiibaam
for i in range(0,Nt):  
  videja_vertiba[i]= u[int((punkti-1)/2),i+1]

print("videja_vertiba: ", videja_vertiba[:])
axs[2].plot(videja_vertiba[:], 'bo')
axs[2].plot(videja_vertiba[:], 'b--')

#-------------------------------------------------------------------------------------
# asu un grafiku nofromeejums
axs[0].set_xlabel("x", fontsize='15', loc='right')
axs[0].set_ylabel("t", fontsize='15',  rotation=0, loc='top')
axs[0].set_title("Funkcijas grafiks", fontsize='15')
axs[1].set_title("Nx = 100; Nt = 100", fontsize='15')
axs[2].set_title("Nx = 100; Nt = 100", fontsize='15')
axs[1].set_xlabel("x", fontsize='15', loc='right')
axs[1].set_ylabel("t", fontsize='15', rotation=0, loc='top')
axs[2].set_xlabel("x", fontsize='15', loc='right')
axs[2].set_ylabel("t", fontsize='15', rotation=0, loc='top')

plt.show()