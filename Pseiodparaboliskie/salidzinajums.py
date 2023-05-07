import matplotlib.pyplot as plt
import numpy as np
import math

#nodefinē funkciju
def y(x):
  return np.sin(np.pi*x)

#--------------------------------------------------------------------------------------
#MAINIIGIE
# funkcijas intervaals uz x ass
intervals = 1
# sadalījums uz x ass
Nx = 10
# sadaliijums uz t ass
Nt = 1
# cikla izpildes reizu skaits
l = Nt + 1
# apreekina sadaliijuma soli uz x ass
h = intervals/Nx
#apreekina cik punktos tiek sadaliita x ass
punkti = int(intervals/h + 1)

Ʈ=h
γ=Ʈ/h**2
σ = 1

#--------------------------------------------------------------------------------------
# intervaals grafika atteelosanai
fx = np.linspace(0, intervals)
fy = y(fx)
# sadala x veertiibas atkariibaa no intervaala un sadaiijuma sola h
x = np.arange(0, intervals + h, h)
#aprekina funkcijas vērtības
y = y(x)

#---------------------------------------------------------------------------------------
# η=1
η=1

#IZVEIDO NULLU MATRICAS
# u matricaa saglabaa apreekinaataas tuvinaatas vertiibas
u = np.zeros((punkti,l))
alpha = np.zeros((punkti,l))
beta = np.zeros((punkti,l))

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

print("η=1", u[:,:])

#---------------------------------------------------------------------------------------
# konstruē grafiku funkcijas patieso veetiibu grafiku
plt.plot(u[:,0], 'ro')
plt.plot(u[:,0], 'r--')

# konstruē η=1 grafiku
plt.plot(u[:,1], 'bo')
plt.plot(u[:,1], 'b--')

#---------------------------------------------------------------------------------------
# η=0
η=0

#IZVEIDO NULLU MATRICAS
alpha = np.zeros((punkti,l))
beta = np.zeros((punkti,l))
# saglabaa u matricaa funkcijas preciizaas veertiibas
for i in range(0,punkti-1):
  u[i,0] = y[i]
#---------------------------------------------------------------------------------------
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

print("η=0", u[:,:])

#---------------------------------------------------------------------------------------
# konstruē η=0 grafiku
plt.plot(u[:,1], 'go')
plt.plot(u[:,1], 'g--')

#-------------------------------------------------------------------------------------
# asu un grafiku nofromeejums
plt.xlabel("x", fontsize='10', loc='right')
plt.ylabel("t", fontsize='10',  rotation=0, loc='top')

plt.show()