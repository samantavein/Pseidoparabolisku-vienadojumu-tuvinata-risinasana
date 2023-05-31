import matplotlib.pyplot as plt
import numpy as np

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
#mainigais sigma
σ = 0.1
# intervals [0;eta]
eta = 1
# intervala [0;sigma] sadalijuma soļu skaits
N_eta = 4

#-------------------------------------------------------------------------------------
# sadala x un t veertiibas atkariibaa no intervaala 
# x vērtības intervalaa [0;L]
x = np.arange(0, L + h, h)
# t vērtības intervalaa [0;T]
t = np.arange(0, T + Ʈ, Ʈ)
# η vērtības intervalaa [0;eta]
η = np.arange(0,  eta +  eta/N_eta, 1/N_eta)

print("x:", x)
print("t:", t)
print("η:", η)

print("--------------------------------------------------------------------------")
#IZVEIDO NULLU MATRICAS
# u matricaa tiks saglabatas apreekinaataas tuvinaatas vertiibas
u = np.zeros((Nx+1,Nt+1))
# matricaas tiks saglabaatas alpha un beta vertibas vertiibas
alpha = np.zeros((Nx+1,Nt+1))
beta = np.zeros((Nx+1,Nt+1))
# u2 matricaa tiks saglabatas apreekinaataas tuvinaatas vertiibas visos eta gadijumos
u2 = np.zeros((Nx+1,N_eta+1))
# videja_vertiba matrica ,kura tiks saglabatas tuvinatas vertibas no intervala [0;L] viduspunta
videjas_vertibas=np.zeros((Nt+1))
# tiks saglabatas kluudas
kluda = np.zeros((Nx+1, N_eta+1))

# u matricaa saglabaa analitiskas vertiibas
u_a= np.zeros((Nx+1,Nt+1))
u2_a = np.zeros((Nx+1,N_eta+1))
# videja_vertiba matrica ,kura tiks saglabatas analitiskas vertibas no intervala [0;L] viduspunta
videjas_vertibas_a=np.zeros((Nt+1))

#sakuma nosacijums
u[:,0] = np.sin(np.pi*x)
# robeznosacijumi
u[0,0] = 0
u[Nx,0] = 0

#-------------------------------------------------------------------------------------
#TUVINATO VERTIBU APREKINASANA
for n in range(N_eta + 1):
  
  for j in range (0,Nt):
    # reekina alpha un beta
    for i in range(1,Nx):   
      A= (γ*σ + η[n]*(γ/Ʈ))
      B= (γ*σ + η[n]*(γ/Ʈ))
      C= (1 + 2*γ*σ + 2*η[n]*(γ/Ʈ))
      F =(((1-σ)*γ - η[n]*(γ/Ʈ)) * u[i-1,j] + (1 - 2*(1-σ)*γ + 2*η[n]*(γ/Ʈ)) * u[i,j] + ((1-σ)*γ - η[n]*(γ/Ʈ)) * u[i+1,j])

      alpha[i+1,j] = B/(C - A * alpha[i,j])     
      beta[i+1,j] = (A*beta[i,j]+F)/(C-A*alpha[i,j])

    #reekina tuvinaataas veertiibas
    for i in range(Nx-1,0,-1):
      u[i,j+1] = alpha[i+1,j]*u[i+1,j+1]+beta[i+1,j]

 #-------------------------------------------------------------------------------------
  # Analitiskie apreini
  for j in range (0, Nt+1):
      for i in range (1,Nx):
        u_a[i,j] = np.e**(-((np.pi**2) / (1 + η[n]*(np.pi**2))) * t[j] ) * np.sin(np.pi*x[i])
  
  # aizpilda matricas ar tuvinatajiem un analitiskajiem rezultatiem, kad t=T un aprekina kludas
  for i in range(0,Nx+1):
    u2[i,n] = u[i,Nt]
    u2_a[i,n] = u_a[i,Nt]
    kluda[i,n] = abs(u2_a[i,n] - u2[i,n])
  #-------------------------------------------------------------------------------------
  
  #izprinte tuvinatas vertibas un kludas katraa eta gadijumaa
  print("η=",η[n])
  print("u(",j,")",u2[:,n])
  print("u(",j,")",u2_a[:,n])
  print("kluda:", kluda[:,n])

#KONSTRUE GRAFIKUS
# analitiska un tuvinata likne, kad eta = 0
plt.plot(u2_a[:,0], 'r-',linewidth = '5')
#axs[0].plot(u2[:,0], 'bo')
plt.plot(u2[:,0], 'b--',linewidth = '3')

# analitiskas un tuvinatas liknes, kad 0 < eta < 1
for i in range (1,N_eta):
  plt.plot(u2_a[:,i], 'r-',linewidth = '5')
  #axs[0].plot(u2[:,i], 'ko')
  plt.plot(u2[:,i], 'y--',linewidth = '3')

# analitiska un tuvinata likne, kad sigma = 1
plt.plot(u2_a[:,N_eta], 'r-',linewidth = '5')
#axs[0].plot(u2[:,N_eta], 'go')
plt.plot(u2[:,N_eta], 'g--',linewidth = '3')


#-----------------------------------------------------------------------------------------------------------
plt.xticks(np.linspace(0, Nx, 5), np.linspace(0, L, 5))
plt.xlabel("x", fontsize='20', loc='right')
plt.ylabel("u(x,t)", fontsize='20', rotation=0, loc='top')

plt.tick_params(axis='x', labelsize=13)
plt.tick_params(axis='y', labelsize=13)

plt.show()

# TABULAS IZVEIODSANA UN IZVADISANA
import plotly.graph_objects as go

fig = go.Figure(data=[go.Table(
                      columnwidth = [50,100],
                      header=dict(values=['x', 'Analītiski iegūtā atrisinājuma vērtības', 'η = 0.0','∆1', 'Analītiski iegūtā atrisinājuma vērtības', 'η = 0.5','∆2', 'Analītiski iegūtā atrisinājuma vērtības', 'η = 1.0', '∆3'],
                      font=dict(color='black', size=15),line_color='darkslategray',height=35),
                      cells=dict(values=[np.round(x[::int(Nx/10)],2), 
                                         np.round(u2_a[::int(Nx/10),0],10), np.round(u2[::int(Nx/10),0],10), np.round(kluda[::int(Nx/10),0],10), 
                                         np.round(u2_a[::int(Nx/10),2],10), np.round(u2[::int(Nx/10),2],10), np.round(kluda[::int(Nx/10),2],10),
                                         np.round(u2_a[::int(Nx/10),4],10), np.round(u2[::int(Nx/10),4],10), np.round(kluda[::int(Nx/10),4],10)],
                                  height=30,line_color='darkslategray',fill_color='white',
                                  font=dict(color='black', size=14)))
                     ])
fig.show()