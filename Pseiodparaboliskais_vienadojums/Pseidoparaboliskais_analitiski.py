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
Nx = 40
# intervala [0;T] sadalijuma soļu skaits
Nt = 1000
# intervala [0;L] soļa garums
h = L / Nx
# intervala [0;T] soļa garums
Ʈ = T / Nt
# mainigais eta
η = 1

# x vērtības intervalaa [0;L]
x = np.arange(0, L + h, L/Nx)
# t vērtības intervalaa [0;T]
t = np.arange(0, T + Ʈ, T/Nt)
print("x:", x)
print("t:", t)
print("-----------------------------------------------------------------------------")

#-------------------------------------------------------------------------------------
#IZVEIDO NULLU MATRICAS
# u matricaa saglabaa analitiskas vertiibas
u = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas vertibas no intervala [0;L] viduspunta
videja_vertiba = np.zeros((Nt+1))

#-------------------------------------------------------------------------------------
#analitisko vertibu aprekinasana
for j in range (0, Nt+1):
  for i in range (0,Nx):
    u[i,j] = np.e**(- ((np.pi**2)/(1 + η*(np.pi**2))) * t[j] ) * np.sin(np.pi*x[i])

# saglaba matrica vertibas no intervala [0;L] viduspunta
for i in range(0,Nt+1):  
  videja_vertiba[i]= u[int(Nx/2),i]
print("videja_vertiba: ", videja_vertiba[::int(Nt/10)])

#izprinte pirmo u(x,t) liimeni ar analitiskajam vertibam, kad t[1]
print("u(1)", u[::int(Nx/10),1])
#-------------------------------------------------------------------------------------
# KONSTRUEE GRAFIKUS
axs[0].plot(u[:,0], 'r-', linewidth='4')
# konstrue analītisko aprekinu liknes
for i in range(1,Nt+1, int(Nt/10)):
  #axs[0].plot(u[:,i], 'bo')
  axs[0].plot(u[:,i], 'b--',linewidth = '2.5')

# sakumnosacijuma likne
#axs[0].plot(u[:,0], 'ro')


# konstrue grafiku ar vertibam no intervala [0;L] viduspunta
axs[1].plot(videja_vertiba[:], 'b-', linewidth = '4')

# sadala un pieskir x asiim veertiibas un iedod x un y asiim nosaukumus
axs[0].set_xticks(np.linspace(0, Nx, 5)) 
axs[0].set_xticklabels(np.linspace(0, L, 5))  
axs[0].set_xlabel("x", fontsize='20', loc='right')
axs[0].set_ylabel("u(x,t)", fontsize='20', rotation=0, loc='top')

#axs[0].set_xlim((14,26))
#axs[0].set_ylim((0.7,1.1))

axs[0].tick_params(axis='x', labelsize=15)
axs[0].tick_params(axis='y', labelsize=15)

axs[1].set_xticks(np.linspace(0, Nt, 11)) 
axs[1].set_xticklabels(np.linspace(0, T, 11))  
axs[1].set_xlabel("t", fontsize='20', loc='right')
axs[1].set_ylabel("u(x,t)", fontsize='20', rotation=0, loc='top')

axs[1].tick_params(axis='x', labelsize=15)
axs[1].tick_params(axis='y', labelsize=15)

# izveido un uzkonstruee virsmas grafiku
X, T = np.meshgrid(x, t)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, u.T, cmap='viridis')

ax.set_xlabel('x',fontsize='15')
ax.set_ylabel('t',fontsize='15')
ax.set_zlabel('u(x, t)',fontsize='15')

plt.show()