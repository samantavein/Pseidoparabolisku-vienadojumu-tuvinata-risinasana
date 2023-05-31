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
#mainigais eta
η = 1
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

#sakuma nosacijums
u[:,0] = np.sin(np.pi*x)
# robeznosacijumi
u[0,0] = 0
u[Nx,0] = 0

# Analitiskie apreini
for j in range (0, Nt+1):
  for i in range (1,Nx):
    u_a[i,j] = np.e**(-((np.pi**2) / (1 + η*(np.pi**2))) * t[j] ) * np.sin(np.pi*x[i])

#-------------------------------------------------------------------------------------
#TUVINATO VERTIBU APREKINASANA
for n in range(N_sigma + 1):
  for j in range (0,Nt):
    # reekina alpha un beta
    for i in range(1,Nx):   
      A= (γ*σ[n] + η*(γ/Ʈ))
      B= (γ*σ[n] + η*(γ/Ʈ))
      C= (1 + 2*γ*σ[n] + 2*η*(γ/Ʈ))
      F =(((1-σ[n])*γ - η*(γ/Ʈ)) * u[i-1,j] + (1 - 2*(1-σ[n])*γ + 2*η*(γ/Ʈ)) * u[i,j] + ((1-σ[n])*γ - η*(γ/Ʈ)) * u[i+1,j])

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
  print("analistsiki", u_a[::int(Nx/10),Nt])
  print("u2",i," :", u2[::int(Nx/10),i])

#KONSTRUE GRAFIKUS
# analitiska likne
plt.plot(u_a[:,Nt], 'r-',linewidth = '5')
# likne, kad sigma = 0
plt.plot(u2[:,0], 'bo')
plt.plot(u2[:,0], 'b--',linewidth = '3')

# liknes, kad 0 < sigma < 1
for i in range (1,N_sigma):  
  plt.plot(u2[:,i], 'ko')
  plt.plot(u2[:,i], 'k--',linewidth = '2')

# likne, kad sigma = 1
plt.plot(u2[:,N_sigma], 'go')
plt.plot(u2[:,N_sigma], 'g--',linewidth = '3')

# sadala un pieskir x asiim veertiibas un iedod x un y asiim nosaukumus
plt.xticks(np.linspace(0, Nx, 5), np.linspace(0, L, 5))
plt.xlabel("x", fontsize='15', loc='right')
plt.ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

# ierobezo vertibas uz x un y asiim, lai pietuvinaatu grafiku
#plt.xlim((19.999,20.001))
#plt.ylim((0.91318,0.91322))

plt.show()

# TABULAS IZVEIODSANA UN IZVADISANA
import plotly.graph_objects as go

fig = go.Figure(data=[go.Table(
                      columnwidth = [40,100,100,80,100,80,100],
                      header=dict(values=['x', 'Analītiski iegūtā atrisinājuma vērtības', 'σ = 0.0','∆ (0.0)', 'σ = 0.1','∆ (0.1)','σ = 0.5','∆ (0.5)','σ = 0.9','∆ (0.9)','σ = 1.0','∆ (1.0)'],
                      font=dict(color='black', size=16),line_color='darkslategray',height=35),
                      cells=dict(values=[np.round(x[::int(Nx/10)],2), np.round(u_a[::int(Nx/10),Nt],9), 
                                         np.round(u2[::int(Nx/10),0],10), np.round(kluda[::int(Nx/10),0],12), 
                                         np.round(u2[::int(Nx/10),1],10), np.round(kluda[::int(Nx/10),1],12),
                                         np.round(u2[::int(Nx/10),5],10), np.round(kluda[::int(Nx/10),5],10),
                                         np.round(u2[::int(Nx/10),9],10), np.round(kluda[::int(Nx/10),9],10),
                                         np.round(u2[::int(Nx/10),10],10), np.round(kluda[::int(Nx/10),10],10),
                                         ],
                                  height=30,line_color='darkslategray',fill_color='white',
                                  font=dict(color='black', size=14)))
                     ])
fig.show()