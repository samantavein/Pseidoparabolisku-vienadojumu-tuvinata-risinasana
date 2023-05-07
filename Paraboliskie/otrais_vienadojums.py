import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(25, 5))

#nodefinee funkciju
def y(x):
  return -x**2 + 4*x

#--------------------------------------------------------------------------------------
#MAINIIGIE
# funkcijas intervaals uz x ass
intervals = 4
# sadalījums uz x ass
Nx= 4
# sadaliijums uz t ass
Nt= 10
# cikla izpildes reizu skaits
l=Nt+1
# apreekina sadaliijuma soli uz x ass
h = intervals/Nx
#apreekina cik punktos tiek sadaliita x ass
punkti = int(intervals/h + 1)

Ʈ = h
γ = Ʈ / (h**2)
σ = 1

#-------------------------------------------------------------------------------------
# intervaals grafika atteelosanai
fx = np.linspace(0, intervals)
fy = y(fx)
# sadala x veertiibas atkariibaa no intervaala un sadaiijuma sola h
x = np.arange(0, intervals + h, h)
#aprekina funkcijas vērtības
y = y(x)

#izprintee ieguutas x, y veertiibas, uzzkonstruee funkcijas grafiku ar preciizajaam veertiibaam
print("x:", x, "y:", y)
axs[0].plot(x, y, 'ro')
axs[0].plot(fx, fy, '--')
print("γ=",γ)

#-------------------------------------------------------------------------------------
#IZVEIDO NULLU MATRICAS
# u matricaa saglabaa apreekinaataas tuvinaatas vertiibas
u = np.zeros((punkti,l))
alpha = np.zeros((punkti,l))
beta = np.zeros((punkti,l))
videjas_vertibas = np.zeros((l))

# saglabaa u matricaa funkcijas preciizaas veertiibas
for i in range(0,punkti-1):
  u[i,0] = y[i]

#-------------------------------------------------------------------------------------
#Tuvinato veertiibu apreekinaasana
for j in range (1,l):
  # reekina alpha un beta
  for i in range(0,punkti-2):   
    alpha[i+1,j] = (γ*σ)/((1+2*γ*σ)-(γ*σ*alpha[i,j]))
    beta[i+1,j] = (γ*σ*beta[i,j]+u[i+1,j-1])/((1+2*γ*σ)-(γ*σ*alpha[i,j]))

  #reekina tuvinaataas veertiibas
  for i in range(punkti-2,0,-1):
    u[i,j] = alpha[i,j]*u[i+1,j]+beta[i,j]

#-------------------------------------------------------------------------------------
# KONSTRUEE GRAFIKUS
# funkcijas preciizais grafiks
axs[1].plot(u[:,0], 'ro')
axs[1].plot(u[:,0], 'r--')
print("u(0)", u[:,0])

#funkcijas grafiki ar apreekinaatajaam tuvinaatajaam vertiibaam
for i in range(1,l):
  axs[1].plot(u[:,i], 'bo')
  axs[1].plot(u[:,i], 'b--')
  print("u(",i,")", u[:,i])

#grafiks ar funcijas videejaam vertiibaam
for i in range(Nt):
  videjas_vertibas[i]= u[int((punkti-1)/2),i+1]

print("videjas_vertibas: ", videjas_vertibas[:]) 
axs[2].plot(videjas_vertibas[:], 'bo')
axs[2].plot(videjas_vertibas[:], 'b--')

#-------------------------------------------------------------------------------------
# asu un grafiku nofromeejums
axs[0].set_xlabel("x", fontsize='15', loc='right')
axs[0].set_ylabel("t", fontsize='15',  rotation=0, loc='top')
axs[0].set_title("Funkcijas grafiks", fontsize='15')
axs[1].set_title("Nx = 4; Nt = 10", fontsize='15')
axs[2].set_title("Nx = 4; Nt = 10", fontsize='15')
axs[1].set_xlabel("x", fontsize='15', loc='right')
axs[1].set_ylabel("t", fontsize='15', rotation=0, loc='top')
axs[2].set_xlabel("x", fontsize='15', loc='right')
axs[2].set_ylabel("t", fontsize='15', rotation=0, loc='top')

plt.show()