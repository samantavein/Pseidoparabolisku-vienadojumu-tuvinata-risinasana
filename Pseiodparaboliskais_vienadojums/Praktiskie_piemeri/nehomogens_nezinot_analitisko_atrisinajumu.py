import matplotlib.pyplot as plt
import numpy as np
plt.axhline(y=0, color='k', linestyle='-', linewidth='0.5')
#--------------------------------------------------------------------------------------
#MAINIIGIE
# intervals [0;L]
L = 10
# intervals [0;T]
T = 0.5
# intervala [0;L] sadalijuma soļu skaits
Nx = 20
# intervala [0;T] sadalijuma soļu skaits
Nt= 1000
# intervala [0;L] soļa garums
h = L / Nx
# intervala [0;T] soļa garums
Ʈ = T / Nt
# apreekina mainiigo gamma
γ = Ʈ / (h**2)
print("γ=",γ)
# mainigais sigma
σ = 0
# mainigais eta
η = 1

print("-----------------------------------------------------------------------------")

# x vērtības intervalaa [0;L]
x = np.arange(0, L + h, h)
# t vērtības intervalaa [0;T]
t = np.arange(0, T + Ʈ, Ʈ)
print("x:", x)
print("t:", t)
print("-----------------------------------------------------------------------------")

#-------------------------------------------------------------------------------------
# TUVINATA RISINASANA
#-------------------------------------------------------------------------------------

#IZVEIDO NULLU MATRICAS
# u matricaa tiks saglabatas apreekinaataas tuvinaatas vertiibas
u = np.zeros((Nx+1,Nt+1))
# matricaas tiks saglabaatas alpha un beta vertibas vertiibas
alpha = np.zeros((Nx+1,Nt+1))
beta = np.zeros((Nx+1,Nt+1))

# saakuma nosaciijums 
u[:,0] = 0.05*(x-0)*(x-2)*(x-6.5)*(x-10)
# robeznosacijumi
u[0,0] = 0
u[Nx,0] = 0

#-------------------------------------------------------------------------------------
# TUVINATO VERTIBU APREKINASANA
for j in range (0,Nt):
  # reekina alpha un beta
  for i in range(1,Nx):   
    A= γ*σ + η*(γ/Ʈ)
    B= γ*σ + η*(γ/Ʈ)
    C= 1 + 2*γ*σ + 2*η*(γ/Ʈ)

    fx = np.e**(4*t[j+1]) -(np.sqrt(2*x[i])) * (x[i]-5)/(2+(t[j+1]**2)) + 2**((-6*t[j+1])/(5*x[i])) + (x[i]**(-0.5)-4)*0.5*t[j+1]**x[i]*np.e**(5*t[j+1])

    F = ((1-σ)*γ - η*(γ/Ʈ)) * u[i-1,j] + (1 - 2*(1-σ)*γ + 2*η*(γ/Ʈ)) * u[i,j] + ((1-σ)*γ - η*(γ/Ʈ)) * u[i+1,j] + Ʈ * fx

    alpha[i+1,j] = B/(C-A*alpha[i,j])
    beta[i+1,j] = (A*beta[i,j]+F)/(C-A*alpha[i,j])

  #reekina tuvinaataas veertiibas
  for i in range(Nx-1,0,-1):
    u[i,j+1] = alpha[i+1,j]*u[i+1,j+1]+beta[i+1,j]

#izprinte pirmo u(x,t) liimeni ar tuvinatajam vertibam, kad t[1]
print("u(1)", u[::int(Nx/10),1])

#-------------------------------------------------------------------------------------
# KONSTRUEE GRAFIKUS

# konstrue tuvinaato veertiibu liknes
for i in range(1,Nt+1,int(Nt/10) ):
  plt.plot(u[:,i], 'bo')
  plt.plot(u[:,i], 'b--', linewidth='2')

# konstrue sakuma nosacijuma likni
plt.plot(u[:,0], 'ro')
plt.plot(u[:,0], 'r--', linewidth='2')

# sadala un pieskir x asiim veertiibas un iedod x un y asiim nosaukumus
plt.xticks(np.linspace(0, Nx, 5), np.linspace(0, L, 5))
plt.xlabel("x", fontsize='15', loc='right')
plt.ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')


# izveido un uzkonstruee virsmas grafiku
X, T = np.meshgrid(x, t)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, u.T, cmap='viridis')

ax.set_xlabel('x',fontsize='15')
ax.set_ylabel('t',fontsize='15')
ax.set_zlabel('u(x, t)',fontsize='15')

plt.show()

# TABULAS IZVEIODSANA UN IZVADISANA
import plotly.graph_objects as go


# tabula ar tuvinatam vertibam, kad t[1] (t=T/Nt)
fig = go.Figure(data=[go.Table(
                      columnwidth = [50,70,100],
                      header=dict(values=['x','u(x;0)', 'u(x;0,1)','u(x;0,2)','u(x;0,3)','u(x;0,4)','u(x;0,5)'],
                      font=dict(color='black', size=15),line_color='darkslategray',height=35),
                      cells=dict(values=[np.round(x[::int(Nx/10)],2),  
                                         np.round(u[::int(Nx/10),0],12),
                                         np.round(u[::int(Nx/10),200],12),
                                         np.round(u[::int(Nx/10),400],12),
                                         np.round(u[::int(Nx/10),600],12),
                                         np.round(u[::int(Nx/10),800],12),
                                        np.round(u[::int(Nx/10),1000],12),
                                                                   
                                   ],
                                  
                                  font=dict(color='black', size=14),
                                  height=29,line_color='darkslategray',fill_color='white'))
                     ])
fig.show()