import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(25, 5))
axs[0].axhline(y=0, color='k', linestyle='-', linewidth='0.5')
#--------------------------------------------------------------------------------------
#MAINIIGIE
# intervals [0;L]
L = 1
# intervals [0;T]
T = 1
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
# ANALITISKA RISINASANA
#-------------------------------------------------------------------------------------

#IZVEIDO NULLU MATRICAS
# u matricaa saglabaa analitiskas vertiibas
u_a = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas vertibas, nemot kadu fiksetu punktu intervala [0;L]
videja_vertiba_a = np.zeros((Nt+1))
videja_vertiba_a1 = np.zeros((Nt+1))

#-------------------------------------------------------------------------------------
#analitisko vertibu aprekinasana
for j in range (0, Nt+1):
  for i in range (1,Nx):
    u_a[i,j] = np.cos(t[j])*(9*x[i]**3 - 14.4*x[i]**2 + 5.4*x[i])


# saglaba matricas analitiskas vertibas no intervala [0;L] punktiem x = 0,2 un x = 0,8
for i in range(0,Nt+1):  
  videja_vertiba_a[i]= u_a[4,i]
  videja_vertiba_a1[i]= u_a[16,i]

#-------------------------------------------------------------------------------------
# TUVINATA RISINASANA
#-------------------------------------------------------------------------------------

#IZVEIDO NULLU MATRICAS
# u matricaa tiks saglabatas apreekinaataas tuvinaatas vertiibas
u = np.zeros((Nx+1,Nt+1))
# matricaas tiks saglabaatas alpha un beta vertibas vertiibas
alpha = np.zeros((Nx+1,Nt+1))
beta = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas vertibas, nemot kadu fiksetu punktu intervala [0;L]
videja_vertiba = np.zeros((Nt+1))
videja_vertiba1 = np.zeros((Nt+1))
# kludu matricas
kluda1=np.zeros(Nx+1)
kluda2=np.zeros((Nt+1,2))

# saakuma nosaciijums 
u[:,0] = 9*x**3 - 14.4*x**2 + 5.4*x
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
    F = ((1-σ)*γ - η*(γ/Ʈ)) * u[i-1,j] + (1 - 2*(1-σ)*γ + 2*η*(γ/Ʈ)) * u[i,j] + ((1-σ)*γ - η*(γ/Ʈ)) * u[i+1,j] + Ʈ*(-np.sin(t[j+1])*( 9*x[i]**3 - 14.4*x[i]**2 + 5.4*x[i]) + (54*x[i]-28.8)*(np.sin(t[j+1])-np.cos(t[j+1])) )

    alpha[i+1,j] = B/(C-A*alpha[i,j])
    beta[i+1,j] = (A*beta[i,j]+F)/(C-A*alpha[i,j])

  #reekina tuvinaataas veertiibas
  for i in range(Nx-1,0,-1):
    u[i,j+1] = alpha[i+1,j]*u[i+1,j+1]+beta[i+1,j]

#izprinte pirmo u(x,t) liimeni ar tuvinatajam vertibam, kad t[1]
print("u(1)", u[::int(Nx/10),1])

#aprekina kludas pirmaja limeni, kad t[Nt]
for i in range (0,Nx+1):
  kluda1[i] = abs(u_a[i,Nt]-u[i,Nt])

# saglaba matricas tuvinatas vertibas no intervala [0;L] punktiem x = 0,2 un x = 0,8
for i in range(0,Nt+1):  
  videja_vertiba[i]= u[4,i]
  videja_vertiba1[i]=u[16,i]
  # aprekina kludas
  kluda2[i,0]=abs(videja_vertiba_a[i]-videja_vertiba[i])
  kluda2[i,1]=abs(videja_vertiba_a1[i]-videja_vertiba1[i])

#-------------------------------------------------------------------------------------
# KONSTRUEE GRAFIKUS

# konstrue sakuma nosacijuma likni
axs[0].plot(u[:,0], 'k-', linewidth='4')

# konstrue tuvinaato veertiibu un analitisko vertibu liiknes 
for i in range(1,Nt+1,int(Nt/10) ):
  axs[0].plot(u_a[:,i], 'r-', linewidth='3')
  axs[0].plot(u[:,i], 'bo')
  axs[0].plot(u[:,i], 'b--', linewidth='1.5')


# konstrue grafiku ar vertibam, kad fiksets punkts pukts x=0,2
axs[1].plot(videja_vertiba_a[:], 'r', linewidth='5')
axs[1].plot(videja_vertiba[:], 'b--',linewidth='4')

# konstrue grafiku ar vertibam, kad fiksets punkts x=0,8
axs[2].plot(videja_vertiba_a1[:], 'r', linewidth='5')
axs[2].plot(videja_vertiba1[:], 'b--',linewidth='4')

# sadala un pieskir x asiim veertiibas un iedod x un y asiim nosaukumus
axs[0].set_xticks(np.linspace(0, Nx, 5)) 
axs[0].set_xticklabels(np.linspace(0, L, 5))  
axs[0].set_xlabel("x", fontsize='15', loc='right')
axs[0].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')


#axs[0].set_xlim((4.955,5.045))
#axs[0].set_ylim((0.585,0.595))


axs[1].set_xticks(np.linspace(0, Nt, 5)) 
axs[1].set_xticklabels(np.linspace(0, T, 5))  
axs[1].set_xlabel("t", fontsize='15', loc='right')
axs[1].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

axs[2].set_xticks(np.linspace(0, Nt, 5)) 
axs[2].set_xticklabels(np.linspace(0, T, 5))  
axs[2].set_xlabel("t", fontsize='15', loc='right')
axs[2].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

# izveido un uzkonstruee virsmas grafiku
X, T = np.meshgrid(x, t)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, u_a.T, cmap='viridis')

ax.set_xlabel('x',fontsize='15')
ax.set_ylabel('t',fontsize='15')
ax.set_zlabel('u(x, t)',fontsize='15')

plt.show()

# TABULAS IZVEIODSANA UN IZVADISANA
import plotly.graph_objects as go

# tabula ar tuvinatajam vertibam fiksetos punktos x=0,2 un x=0,8
fig = go.Figure(data=[go.Table(
                      columnwidth = [50,100],
                      header=dict(values=['t','Analītiski iegūtā atrisinājuma vērtības', 'u(0.2,t)', '∆','Analītiski iegūtā atrisinājuma vērtības', 'u(0.8,t)', '∆'  ],
                      font=dict(color='black', size=15),line_color='darkslategray'),
                      cells=dict(values=[np.round(t[::int(Nt/10)],2), 
                                    np.round(videja_vertiba_a[::int(Nt/10)],12),  np.round(videja_vertiba[::int(Nt/10)],9), np.round(kluda2[::int(Nt/10),0],12),
                                    np.round(videja_vertiba_a1[::int(Nt/10)],12),  np.round(videja_vertiba1[::int(Nt/10)],9), np.round(kluda2[::int(Nt/10),1],12)],
                                  font=dict(color='black', size=14),
                                  height=29,line_color='darkslategray',fill_color='white'))
                     ])
fig.show()

# tabula ar tuvinatam vertibam, kad t[1] (t=T/Nt)
fig = go.Figure(data=[go.Table(
                      columnwidth = [50,100],
                      header=dict(values=['x','Analītiski iegūtā atrisinājuma vērtības', 'u(x,1)', '∆' ],
                      font=dict(color='black', size=15),line_color='darkslategray',height=35),
                      cells=dict(values=[np.round(x[::int(Nx/10)],2), np.round(u_a[::int(Nx/10),Nt],12),  
                                   np.round(u[::int(Nx/10),Nt],12), np.round(kluda1[::int(Nx/10)],12)],
                                  font=dict(color='black', size=14),
                                  height=29,line_color='darkslategray',fill_color='white'))
                     ])
fig.show()