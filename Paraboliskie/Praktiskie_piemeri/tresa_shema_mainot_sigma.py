import matplotlib.pyplot as plt
import numpy as np
import math
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
Ʈ = T/Nt
# apreekina mainiigo gamma
γ = Ʈ / (h**2)
print("γ=",γ)

# intervals [0;sigma]
sigma = 1
# intervala [0;sigma] sadalijuma soļu skaits
N_sigma = 10

#-------------------------------------------------------------------------------------
# x vērtības intervalaa [0;L]
x = np.arange(0, L + h, h)
# t vērtības intervalaa [0;T]
t = np.arange(0, T + Ʈ, Ʈ)
# σ vērtības intervalaa [0;sigma]
σ = np.arange(0, sigma +  sigma/N_sigma, 1/N_sigma)

print("x:", x)
print("t:", t)
print("σ:", σ)

print("--------------------------------------------------------------------------")
#IZVEIDO NULLU MATRICAS
# u matricaa tiks saglabatas apreekinaataas tuvinaatas vertiibas
u = np.zeros((Nx+1,Nt+1))
# matricaas tiks saglabaatas alpha un beta vertibas vertiibas
alpha = np.zeros((Nx+1,Nt+1))
beta = np.zeros((Nx+1,Nt+1))
# u2 matricaa tiks saglabatas apreekinaataas tuvinaatas vertiibas visos sigma gadijumos
u2 = np.zeros((Nx+1,N_sigma+1))
# videja_vertiba matrica ,kura tiks saglabatas tuvinatas vertibas no intervala [0;L] viduspunta
videjas_vertibas=np.zeros((Nt+1))
# tiks saglabatas kluudas
kluda = np.zeros((Nx+1, N_sigma+1))

# u matricaa saglabaa analitiskas vertiibas
u_a= np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas analitiskas vertibas no intervala [0;L] viduspunta
videjas_vertibas_a=np.zeros((Nt+1))

u[:,0] = np.sin(np.pi*x)
# robeznosacijumi
u[0,0] = 0
u[Nx,0] = 0

# aprekina analitiskas vertibas
for j in range (0, Nt+1):
  for i in range (1,Nx):
    u_a[i,j] = np.e**(-(np.pi**2) * t[j] ) * np.sin(np.pi*x[i])
print("u(a)",u_a[:,1])

#-------------------------------------------------------------------------------------
#TUVINATO VERTIBU APREKINASANA
for n in range(N_sigma + 1):
  for j in range (0,Nt):
    # reekina alpha un beta
    for i in range(1,Nx):   
      A=γ*σ[n]
      B=γ*σ[n]
      C=2*γ*σ[n] + 1
      F = (γ*(1-σ[n]))*u[i-1,j] + (1 - 2*γ*(1-σ[n])) * u[i,j] + (γ*(1-σ[n]))*u[i+1,j]

      alpha[i+1,j] = B/(C - A * alpha[i,j])     
      beta[i+1,j] = (A*beta[i,j]+F)/(C-A*alpha[i,j])

    #reekina tuvinaataas veertiibas un kludas
    for i in range(Nx-1,0,-1):
      u[i,j+1] = alpha[i+1,j]*u[i+1,j+1]+beta[i+1,j]

  for i in range(0,Nx+1):
    u2[i,n] = u[i,Nt]
    kluda[i,n] = abs(u_a[i,Nt] - u2[i,n])
  #-------------------------------------------------------------------------------------

  #izprinte tuvinatas vertibas un kludas katraa sigma gadijumaa
  print("σ=",σ[n])
  print("u(",j,")",u2[:,n])
  print("kluda:", kluda[:,n])
  print("-------------------------------------------------------------------------------")

for i in range(N_sigma+1):
  print("u2",i," :", u2[::int(Nx/10),i])

#KONSTRUE GRAFIKUS
# analitiska likne
axs[0].plot(u_a[:,Nt], 'r-',linewidth = '5')

axs[0].plot(u2[:,0], 'bo')
axs[0].plot(u2[:,0], 'b--',linewidth = '3')

# likne, kad 0 < sigma < 1
for i in range (1,N_sigma):  
  axs[0].plot(u2[:,i], 'ko')
  axs[0].plot(u2[:,i], 'k--',linewidth = '2')

# likne, kad sigma = 1
axs[0].plot(u2[:,N_sigma], 'go')
axs[0].plot(u2[:,N_sigma], 'g--',linewidth = '3')


# sadala un pieskir x asiim veertiibas un iedod x un y asiim nosaukumus
axs[0].set_xticks(np.linspace(0, Nx, 5)) 
axs[0].set_xticklabels(np.linspace(0, L, 5))  
axs[0].set_xlabel("x", fontsize='15', loc='right')
axs[0].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

# ierobezo vertibas uz x un y asiim, lai pietuvinaatu grafiku
axs[0].set_xlim((19.8,20.2))
axs[0].set_ylim((0.37175,0.3735))


plt.show()

# TABULAS IZVEIODSANA UN IZVADISANA
import plotly.graph_objects as go

fig = go.Figure(data=[go.Table(
                      columnwidth = [40,110,100],
                      header=dict(values=['x', 'Analītiski iegūtās atrisinājuma vērtības', 'σ = 0.0','∆ (0.0)', 'σ = 0.1','∆ (0.1)','σ = 0.5','∆ (0.5)','σ = 0.9','∆ (0.9)','σ = 1.0','∆ (1.0)'],
                      font=dict(color='black', size=16),line_color='darkslategray',height=35),
                      cells=dict(values=[np.round(x[::int(Nx/10)],2), np.round(u_a[::int(Nx/10),Nt],9), 
                                         np.round(u2[::int(Nx/10),0],9), np.round(kluda[::int(Nx/10),0],9), 
                                         np.round(u2[::int(Nx/10),1],9), np.round(kluda[::int(Nx/10),1],9),
                                         np.round(u2[::int(Nx/10),5],9), np.round(kluda[::int(Nx/10),5],9),
                                         np.round(u2[::int(Nx/10),9],9), np.round(kluda[::int(Nx/10),9],9),
                                         np.round(u2[::int(Nx/10),10],9), np.round(kluda[::int(Nx/10),10],9),
                                         ],
                                  height=30,line_color='darkslategray',fill_color='white',
                                  font=dict(color='black', size=14)))
                     ])
fig.show()