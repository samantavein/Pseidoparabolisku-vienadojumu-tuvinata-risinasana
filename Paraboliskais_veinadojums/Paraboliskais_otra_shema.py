import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))

#--------------------------------------------------------------------------------------
#MAINIIGIE
# intervals [0;L]
L = 1
# intervals [0;T]
T = 0.1
# intervala [0;L] sadalijuma soļu skaits
Nx= 40
# intervala [0;T] sadalijuma soļu skaits
Nt= 100

# intervala [0;L] soļa garums
h = L / Nx
# intervala [0;T] soļa garums
Ʈ = T / Nt
# apreekina mainiigo gamma
γ = Ʈ / (h**2)
print("γ=",γ)
print("-----------------------------------------------------------------------------")

# x vērtības intervalaa [0;L]
x = np.arange(0, L + h, L/Nx)
# t vērtības intervalaa [0;T]
t = np.arange(0, T + Ʈ, T/Nt)
print("x:", x)
print("t:", t)
print("-----------------------------------------------------------------------------")
#-------------------------------------------------------------------------------------
#IZVEIDO NULLU MATRICAS
# u matricaa tiks saglabatas apreekinaataas tuvinaatas vertiibas
u = np.zeros((Nx+1,Nt+1))
# matricaas tiks saglabaatas alpha un beta vertibas vertiibas
alpha = np.zeros((Nx+1,Nt+1))
beta = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas vertibas no intervala [0;L] viduspunta
videja_vertiba = np.zeros((Nt+1))

# saakuma nosaciijums 
u[:,0] = np.sin(np.pi*x)
# robeznosacijumi
u[0,0] = 0
u[Nx,0] = 0
#------------------------------------------------------------------------------------- 
#TUVINATO VERTIBU APREKINASANA
for j in range (0,Nt):
  # reekina alpha un beta
  for i in range(1,Nx):   
    A = (γ)
    B = (γ)
    C = (2*γ + 1)
    F = u[i,j]

    alpha[i+1,j] = B/(C-A*alpha[i,j])
    beta[i+1,j] = (A*beta[i,j]+F)/(C-A*alpha[i,j])
   
  #reekina tuvinaataas veertiibas
  for i in range(Nx-1,0,-1):
    u[i,j+1] = alpha[i+1,j]*u[i+1,j+1]+beta[i+1,j]

#izprinte pirmo u(x,t) liimeni ar tuvinatajam vertibam, kad t[1]
print("u(1)", u[::int(Nx/10),1])
print("-----------------------------------------------------------------------------")

#izprinte katru desmito u(x,t) liimeni ar tuvinatajam vertibam
for i in range(0, Nt+1, int(Nt/10)):
  print("t(", i,"):",t[i])
  print("u(", i,"):", u[:,i])
  print("-----------------------------------------------------------------------------")

# KONSTRUEE GRAFIKUS
# kostrue liknes ar apreekinaatajaam tuvinaatajaam vertiibaam
for i in range(1,Nt+1, int(Nt/10)):
  axs[0].plot(u[:,i], 'bo')
  axs[0].plot(u[:,i], 'b--')

# sakumnosacijuma likne
axs[0].plot(u[:,0], 'ro')
axs[0].plot(u[:,0], 'r--')

# saglaba matrica vertibas no intervala [0;L] viduspunta
for i in range(0,Nt+1):  
  videja_vertiba[i]= u[int(Nx/2),i]
print("videja_vertiba: ", videja_vertiba[::int(Nt/10)])

# konstrue grafiku ar vertibam no intervala [0;L] viduspunta
axs[1].plot(videja_vertiba[:], 'bo')
axs[1].plot(videja_vertiba[:], 'b--')

# sadala un pieskir x asiim veertiibas un iedod x un y asiim nosaukumus
axs[0].set_xticks(np.linspace(0, Nx, 5)) 
axs[0].set_xticklabels(np.linspace(0, L, 5))  
axs[0].set_xlabel("x", fontsize='15', loc='right')
axs[0].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

axs[1].set_xticks(np.linspace(0, Nt, 5)) 
axs[1].set_xticklabels(np.linspace(0, T, 5))  
axs[1].set_xlabel("t", fontsize='15', loc='right')
axs[1].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

# izveido un uzkonstruee virsmas grafiku
X, T = np.meshgrid(x, t)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, u.T, cmap='viridis')

ax.set_xlabel('x', fontsize='15')
ax.set_ylabel('t', fontsize='15')
ax.set_zlabel('u(x, t)', fontsize='15')

plt.show()