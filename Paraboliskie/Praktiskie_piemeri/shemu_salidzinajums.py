import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(25, 5))

#--------------------------------------------------------------------------------------
#MAINIIGIE
# intervals [0;L]
L = 1
# intervals [0;T]
T = 0.5
# intervala [0;L] sadalijuma soļu skaits
Nx= 10
# intervala [0;T] sadalijuma soļu skaits
Nt= 100
# intervala [0;L] soļa garums
h = L / Nx
# intervala [0;T] soļa garums
Ʈ = T/Nt
# apreekina mainiigo gamma
γ = Ʈ / (h**2)
print("γ=",γ)

#-------------------------------------------------------------------------------------
# x vērtības intervalaa [0;L]
x = np.arange(0, L + h, h)
# t vērtības intervalaa [0;T]
t = np.arange(0, T + Ʈ, Ʈ)
print("x:", x)
print("t:", t)

#-------------------------------------------------------------------------------------
# ANALIITISKIE APREEKINI
# u matricaa saglabaa analitiskas vertiibas
u_a = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas analitiskas vertibas no intervala [0;L] viduspunta
videja_vertiba_a = np.zeros((Nt+1))

# aprekina analitiskas vertibas
for j in range (0, Nt+1):
  for i in range (0,Nx):
    u_a[i,j] = np.e**(- (np.pi**2) * t[j] ) * np.sin(np.pi*x[i])

# saglaba matrica analitiskas vertibas no intervala [0;L] viduspunta
for i in range(0, Nt+1):  
  videja_vertiba_a[i]= u_a[int(Nx/2),i]
#-------------------------------------------------------------------------------------

# PIRMAA SHEEMA
# u matricaa tiks saglabatas apreekinaataas tuvinaatas vertiibas
u1 = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas vertibas no intervala [0;L] viduspunta
videja_vertiba1 = np.zeros((Nt+1))
# mtricas kludaam
kluda1 = np.zeros((Nt+1))
kluda11=np.zeros((Nx+1,2))

# saakuma nosaciijums 
u1[:,0] = np.sin(np.pi*x)
# robeznosacijumi
u1[0,0] = 0
u1[Nx,0] = 0

#------------------------------------------------------------------------------------- 
# TUVINATO VERTIBU APREKINASANA
for j in range(0,Nt):
  for i in range(1, Nx):
      u1[i,j+1] = γ * (u1[i+1,j] - 2 * u1[i,j] + u1[i-1,j]) + u1[i,j]

# saglaba matrica vertibas no intervala [0;L] viduspunta un aprekina kludas
for i in range(0,Nt+1):  
  videja_vertiba1[i]= u1[int(Nx/2),i]
  kluda1[i]= abs(videja_vertiba_a[i] - videja_vertiba1[i])

for i in range(0,Nx+1):
  kluda11[i,0]= abs(u_a[i,1]- u1[i,1])
  kluda11[i,1]= abs(u_a[i,Nt]- u1[i,Nt])
#-------------------------------------------------------------------------------------

# OTRAA SHEEMA
# u matricaa tiks saglabatas apreekinaataas tuvinaatas vertiibas
u2 = np.zeros((Nx+1,Nt+1))
# matricaas tiks saglabaatas alpha un beta vertibas vertiibas
alpha2 = np.zeros((Nx+1,Nt+1))
beta2 = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas vertibas no intervala [0;L] viduspunta
videja_vertiba2 = np.zeros((Nt+1))
# mtricas kludaam
kluda2 = np.zeros((Nt+1))
kluda22=np.zeros((Nx+1,2))

# saakuma nosaciijums 
u2[:,0] = np.sin(np.pi*x)
# robeznosacijumi
u2[0,0] = 0
u2[Nx,0] = 0

#------------------------------------------------------------------------------------- 
# TUVINATO VERTIBU APREKINASANA
for j in range (0,Nt):
    # reekina alpha un beta
  for i in range(1,Nx):   
    A = γ
    B = γ
    C = 2*γ + 1
    F = u2[i,j]
    alpha2[i+1,j] = B/(C-A*alpha2[i,j])
    beta2[i+1,j] = (A*beta2[i,j]+F)/(C-A*alpha2[i,j])

  #reekina tuvinaataas veertiibas
  for i in range(Nx-1,0,-1):
    u2[i,j+1] = alpha2[i+1,j]*u2[i+1,j+1]+beta2[i+1,j]

# saglaba matrica vertibas no intervala [0;L] viduspunta un aprekina kludas
for i in range(0,Nt+1):  
  videja_vertiba2[i]= u2[int(Nx/2),i]
  kluda2[i]= abs(videja_vertiba_a[i] - videja_vertiba2[i])

for i in range(0,Nx+1):
  kluda22[i,0]= abs(u_a[i,1]- u2[i,1])
  kluda22[i,1]= abs(u_a[i,Nt]- u2[i,Nt])
#-------------------------------------------------------------------------------------

# TRESAA SHEEMA
# mainigais sigma
σ = 0.5
# u matricaa tiks saglabatas apreekinaataas tuvinaatas vertiibas
u3 = np.zeros((Nx+1,Nt+1))
# matricaas tiks saglabaatas alpha un beta vertibas vertiibas
alpha3 = np.zeros((Nx+1,Nt+1))
beta3 = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas vertibas no intervala [0;L] viduspunta
videja_vertiba3 = np.zeros((Nt+1))
# mtrica kludaam
kluda3 = np.zeros((Nt+1))
kluda33=np.zeros((Nx+1,2))

# saakuma nosaciijums 
u3[:,0] = np.sin(np.pi*x)
# robeznosacijumi
u3[0,0] = 0
u3[Nx,0] = 0

#------------------------------------------------------------------------------------- 
# TUVINATO VERTIBU APREKINASANA
for j in range (0,Nt):
  # reekina alpha un beta
  for i in range(1,Nx):
    A = γ*σ
    B = γ*σ
    C = 2*γ*σ + 1
    F = (γ*(1-σ))*u3[i-1,j] + (1 - 2*γ*(1-σ)) * u3[i,j] + (γ*(1-σ))*u3[i+1,j]

    alpha3[i+1,j] = B/(C-A*alpha3[i,j])
    beta3[i+1,j] = (A*beta3[i,j]+F)/(C-A*alpha3[i,j])

  #reekina tuvinaataas veertiibas
  for i in range(Nx-1,0,-1):
    u3[i,j+1] = alpha3[i+1,j]*u3[i+1,j+1]+beta3[i+1,j]

# saglaba matrica vertibas no intervala [0;L] viduspunta un aprekina kludas
for i in range(0,Nt+1):  
  videja_vertiba3[i]= u3[int(Nx/2),i]
  kluda3[i]= abs(videja_vertiba_a[i] - videja_vertiba3[i])

for i in range(0,Nx+1):
  kluda33[i,0]= abs(u_a[i,1]- u3[i,1])
  kluda33[i,1]= abs(u_a[i,Nt]- u3[i,Nt])
#-------------------------------------------------------------------------------------
# kostrue liknes ar apreekinaatajaam tuvinaatajaam vertiibaam, kad t[1]
axs[0].plot(u_a[:,1], 'r-', linewidth = '4')
axs[0].plot(u1[:,1], 'b--')
axs[0].plot(u2[:,1], 'g--')
axs[0].plot(u3[:,1], 'y--')

# kostrue liknes ar apreekinaatajaam tuvinaatajaam vertiibaam, kad t[Nt]
axs[1].plot(u_a[:,Nt], 'r-', linewidth = '4')
axs[1].plot(u1[:,Nt], 'b--')
axs[1].plot(u2[:,Nt], 'g--')
axs[1].plot(u3[:,Nt], 'y--')

# konstrue grafiku ar vertibam no intervala [0;L] viduspunta
axs[2].plot(videja_vertiba_a[:], 'r-', linewidth = '4')
axs[2].plot(videja_vertiba1[:], 'b--', linewidth = '2')
axs[2].plot(videja_vertiba2[:], 'g--', linewidth = '2')
axs[2].plot(videja_vertiba3[:], 'y--', linewidth = '2')

# sadala un pieskir x asiim veertiibas un iedod x un y asiim nosaukumus
axs[0].set_xticks(np.linspace(0, Nx, 5)) 
axs[0].set_xticklabels(np.linspace(0, L, 5))  
axs[0].set_xlabel("x", fontsize='15', loc='right')
axs[0].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

axs[1].set_xticks(np.linspace(0, Nx, 5)) 
axs[1].set_xticklabels(np.linspace(0, L, 5))  
axs[1].set_xlabel("x", fontsize='15', loc='right')
axs[1].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

axs[2].set_xticks(np.linspace(0, Nt, 5)) 
axs[2].set_xticklabels(np.linspace(0, T, 5))  
axs[2].set_xlabel("t", fontsize='15', loc='right')
axs[2].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

plt.show()

# TABULU IZVEIODSANA UN IZVADISANA
import plotly.graph_objects as go

# tabula ar analitiskajam un tuvinaatajaam vertiibaam, kad t[1]
fig = go.Figure(data=[go.Table(
                      columnwidth = [50,100],
                      header=dict(values=['x', 'Analītiski','Pirmā shēma', '∆1', 'Otrā shēma','∆2', 'Trešā shēma', '∆3'], 
                                 font=dict(color='black', size=15),line_color='darkslategray', height=35),
                      cells=dict(values=[np.round(x[::int(Nx/10)],2), np.round(u_a[::int(Nx/10),1],9),
                                        np.round(u1[::int(Nx/10),1],9),  np.round(kluda11[::int(Nx/10),0],9), 
                                        np.round(u2[::int(Nx/10),1],9), np.round(kluda22[::int(Nx/10),0],9), 
                                        np.round(u3[::int(Nx/10),1],9), np.round(kluda33[::int(Nx/10),0],9) ],
                                  height=30,line_color='darkslategray',fill_color='white',
                                   font=dict(color='black', size=14) ))
                     ])
fig.show()

# tabula ar analitiskajam un tuvinaatajaam vertiibaam, kad t[Nt]
fig = go.Figure(data=[go.Table(
                      columnwidth = [50,100],
                      header=dict(values=['x', 'Analītiski','Pirmā shēma', '∆1', 'Otrā shēma','∆2', 'Trešā shēma', '∆3'], 
                                 font=dict(color='black', size=15),line_color='darkslategray', height=35),
                      cells=dict(values=[np.round(x[::int(Nx/10)],2), np.round(u_a[::int(Nx/10),Nt],9),
                                        np.round(u1[::int(Nx/10),Nt],9),  np.round(kluda11[::int(Nx/10),1],9), 
                                        np.round(u2[::int(Nx/10),Nt],9), np.round(kluda22[::int(Nx/10),1],9), 
                                        np.round(u3[::int(Nx/10),Nt],9), np.round(kluda33[::int(Nx/10),1],9) ],
                                  height=30,line_color='darkslategray',fill_color='white',
                                   font=dict(color='black', size=14) ))
                     ])
fig.show()

# tabula ar vertibam no intervala [0;L] viduspunta
fig = go.Figure(data=[go.Table(
                      columnwidth = [50,100],
                      header=dict(values=['t', 'Analītiski','Pirmā shēma', '∆1', 'Otrā shēma','∆2', 'Trešā shēma', '∆3'],
                      font=dict(color='black', size=15),line_color='darkslategray', height=35),
                      cells=dict(values=[np.round(t[::int(Nt/10)],2), np.round(videja_vertiba_a[::int(Nt/10)],9),np.round(videja_vertiba1[::int(Nt/10)],9),  
                                    np.round(kluda1[::int(Nt/10)],9), np.round(videja_vertiba2[::int(Nt/10)],9), np.round(kluda2[::int(Nt/10)],9), 
                                    np.round(videja_vertiba3[::int(Nt/10)],9), np.round(kluda3[::int(Nt/10)],9) ],
                                  height=30,line_color='darkslategray',fill_color='white',
                                  font=dict(color='black', size=14)))
                     ])
fig.show()