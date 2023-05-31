import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(20, 10))

#--------------------------------------------------------------------------------------
#MAINIIGIE
#--------------------------------------------------------------------------------------
# intervals [0;L]
L = 1
# intervals [0;T]
T = 0.1
# intervala [0;L] sadalijuma soļu skaits
Nx = 40
# intervala [0;L] soļa garums
h = L / Nx
# x vērtības intervalaa [0;L]
x = np.arange(0, L + h, L/Nx)
print("x:", x[::int(Nx/10)])
#mainigais eta
η = 1
#mainigais sigma
σ = 0

#----------------------------------------------------------------------
#                               Nt = 10
#----------------------------------------------------------------------

# intervala [0;T] sadalijuma soļu skaits
Nt= 10
# intervala [0;T] soļa garums
Ʈ = T / Nt
# t vērtības intervalaa [0;T]
t = np.arange(0, T + Ʈ, T/Nt)
γ = Ʈ / (h**2)
# apreekina mainiigo gamma
print("γ1=",γ)

#-------------------------------------------------------------------------------------
# ANALITIKSI APREKINI, KAD Nt = 10
#------------------------------------------------------------------------------------
# u matricaa saglabaa analitiskas vertiibas
u_a = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas vertibas no intervala [0;L] viduspunta
videja_vertiba_a = np.zeros((Nt+1))

#analitisko vertibu aprekinasana
for j in range (0, Nt+1):
  for i in range (0,Nx):
    u_a[i,j] = np.e**(- ( (np.pi**2) / (1 + η*(np.pi**2)) ) * t[j] ) * np.sin(np.pi*x[i])

# saglabaa matrica vertibas no intervala [0;L] viduspunta
for i in range(0, Nt+1):  
  videja_vertiba_a[i]= u_a[int(Nx/2),i]

#-------------------------------------------------------------------------------------
#TUVIANTO VERTIBU APREKINASANA KAD NT = 10
#-------------------------------------------------------------------------------------

#IZVEIDO NULLU MATRICAS
# u matricaa tiks saglabatas apreekinaataas tuvinaatas vertiibas
u1 = np.zeros((Nx+1,Nt+1))
# matricas kuraas glabaas alpha un beta vertibas
alpha1 = np.zeros((Nx+1,Nt+1))
beta1 = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas vertibas no intervala [0;L] viduspunta
videja_vertiba1 = np.zeros((Nt+1))
#kludu matricas
kluda1 = np.zeros((Nt+1))
kluda12 = np.zeros((Nx+1))

# saakuma nosaciijums 
u1[:,0] = np.sin(np.pi*x)
# robeznosacijumi
u1[0,0] = 0
u1[Nx,0] = 0 

#-------------------------------------------------------------------------------------
#Aprekina tuvinatas vertibas
for j in range (0,Nt):
  #aprekina alpha un beta
  for i in range(1,Nx):   
    A= γ*σ + η*(γ/Ʈ)
    B= γ*σ + η*(γ/Ʈ)
    C= 1 + 2*γ*σ + 2*η*(γ/Ʈ)
    F =((1-σ)*γ - η*(γ/Ʈ)) * u1[i-1,j] + (1 - 2*(1-σ)*γ + 2*η*(γ/Ʈ)) * u1[i,j] + ((1-σ)*γ - η*(γ/Ʈ)) * u1[i+1,j]

    alpha1[i+1,j] = B/(C-A*alpha1[i,j])
    beta1[i+1,j] = (A*beta1[i,j]+F)/(C-A*alpha1[i,j])

  for i in range(Nx-1,0,-1):
    u1[i,j+1] = alpha1[i+1,j]*u1[i+1,j+1]+beta1[i+1,j]

# aprekina kludas liimeni, kad t=Nt
for i in range(0,Nx+1):
  kluda12[i]= abs(u_a[i,Nt] - u1[i,Nt])

# saglaba matrica vertibas no intervala [0;L] viduspunta un aprekina kludas 
for i in range(0,Nt+1):  
  videja_vertiba1[i]= u1[int(Nx/2),i]
  kluda1[i]= abs(videja_vertiba_a[i] - videja_vertiba1[i])

# konstrue grafiku ar vertibam no intervala [0;L] viduspunta
axs[0,0].plot(videja_vertiba_a[:], 'r-', linewidth = '4')
axs[0,0].plot(videja_vertiba1[:], 'b--', linewidth = '3')

# kostrue liknes ar analitiskajam un tuvinaatajaam vertiibaam dazadam
axs[1,0].plot(u_a[:,0], 'r-',linewidth = '6')
for i in range(1,Nt+1,int(Nt/10)):
  axs[1,0].plot(u_a[:,i], 'k-',linewidth = '4')
  #axs[1,0].plot(u12[:,i], 'bo')
  axs[1,0].plot(u1[:,i], 'y--',linewidth = '2')

# sadala un pieskir x asiim veertiibas un iedod x un y asiim nosaukumus
axs[0,0].set_xticks(np.linspace(0, Nt, 11)) 
axs[0,0].set_xticklabels(np.linspace(0, T, 11))  
axs[0,0].set_xlabel("t", fontsize='15', loc='right')
axs[0,0].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

axs[0,0].set_xlim((9.99,10.001))
axs[0,0].set_ylim((0.9125,0.9135))

axs[1,0].set_xticks(np.linspace(0, Nx, 5)) 
axs[1,0].set_xticklabels(np.linspace(0, L, 5))  
axs[1,0].set_xlabel("x", fontsize='15', loc='right')
axs[1,0].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

# ierobezo vertibu intervalus uz asim (pietuvina grafika dalu)
axs[1,0].set_xlim((15,25))
axs[1,0].set_ylim((0.85,1.05))

#----------------------------------------------------------------------
#                               Nt = 100
#----------------------------------------------------------------------

# intervala [0;T] sadalijuma soļu skaits
Nt = 100
# intervala [0;T] soļa garums
Ʈ = T / Nt
# t vērtības intervalaa [0;T]
t = np.arange(0, T + Ʈ, T/Nt)
# apreekina mainiigo gamma
γ = Ʈ / (h**2)
print("γ2=",γ)

#-------------------------------------------------------------------------------------
# ANALITIKSI APREKINI, KAD Nt = 100
#------------------------------------------------------------------------------------

# u matricaa saglabaa analitiskas vertiibas
u_a = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas vertibas no intervala [0;L] viduspunta
videja_vertiba_a = np.zeros((Nt+1))

#analitisko vertibu aprekinasana
for j in range (0, Nt+1):
  for i in range (0,Nx):
    u_a[i,j] = np.e**(- ( (np.pi**2) / (1 + η*(np.pi**2)) ) * t[j] ) * np.sin(np.pi*x[i])

# saglabaa matrica vertibas no intervala [0;L] viduspunta
for i in range(0, Nt+1):  
  videja_vertiba_a[i]= u_a[int(Nx/2),i]

#-------------------------------------------------------------------------------------
#TUVIANTO VERTIBU APREKINASANA KAD NT = 100
#-------------------------------------------------------------------------------------

#IZVEIDO NULLU MATRICAS
# u matricaa tiks saglabatas apreekinaataas tuvinaatas vertiibas
u2 = np.zeros((Nx+1,Nt+1))
# matricas kuraas glabaas alpha un beta vertibas
alpha2 = np.zeros((Nx+1,Nt+1))
beta2 = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas vertibas no intervala [0;L] viduspunta
videja_vertiba2 = np.zeros((Nt+1))
# kludu matricas
kluda2 = np.zeros((Nt+1))
kluda22 = np.zeros((Nx+1))

# saakuma nosaciijums 
u2[:,0] = np.sin(np.pi*x)
# robeznosacijumi
u2[0,0] = 0
u2[Nx,0] = 0 

#-------------------------------------------------------------------------------------
#Aprekina tuvinatas vertibas
for j in range (0,Nt):
  #aprekina alpha un beta
  for i in range(1,Nx):   
    A= γ*σ + η*(γ/Ʈ)
    B= γ*σ + η*(γ/Ʈ)
    C= 1 + 2*γ*σ + 2*η*(γ/Ʈ)
    F =((1-σ)*γ - η*(γ/Ʈ)) * u2[i-1,j] + (1 - 2*(1-σ)*γ + 2*η*(γ/Ʈ)) * u2[i,j] + ((1-σ)*γ - η*(γ/Ʈ)) * u2[i+1,j]

    alpha2[i+1,j] = B/(C-A*alpha2[i,j])
    beta2[i+1,j] = (A*beta2[i,j]+F)/(C-A*alpha2[i,j])

  for i in range(Nx-1,0,-1):
    u2[i,j+1] = alpha2[i+1,j]*u2[i+1,j+1]+beta2[i+1,j]

# aprekina kludas liimeni, kad t=Nt
for i in range(0,Nx+1):
  kluda22[i]= abs(u_a[i,Nt] - u2[i,Nt])

# saglaba matrica vertibas no intervala [0;L] viduspunta un aprekina kludas
for i in range(0,Nt+1):  
  videja_vertiba2[i]= u2[int(Nx/2),i]
  kluda2[i]= abs(videja_vertiba_a[i] - videja_vertiba2[i])

# konstrue grafiku ar vertibam no intervala [0;L] viduspunta
axs[0,1].plot(videja_vertiba_a[:], 'r-', linewidth = '4')
axs[0,1].plot(videja_vertiba2[:], 'b--', linewidth = '3')

# kostrue liknes ar analitiskajam un tuvinaatajaam vertiibaam
axs[1,1].plot(u_a[:,0], 'r-',linewidth = '7')
for i in range(1,Nt+1,int(Nt/10)):
  axs[1,1].plot(u_a[:,i], 'k-',linewidth = '4')
  #axs[1,1].plot(u22[:,i], 'bo')
  axs[1,1].plot(u2[:,i], 'y--',linewidth = '2')

# sadala un pieskir x asiim veertiibas un iedod x un y asiim nosaukumus
axs[0,1].set_xticks(np.linspace(0, Nt, 11)) 
axs[0,1].set_xticklabels(np.linspace(0, T, 11))  
axs[0,1].set_xlabel("t", fontsize='15', loc='right')
axs[0,1].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

axs[0,1].set_xlim((99.9,100.01))
axs[0,1].set_ylim((0.9125,0.9135))

axs[1,1].set_xticks(np.linspace(0, Nx, 5)) 
axs[1,1].set_xticklabels(np.linspace(0, L, 5))  
axs[1,1].set_xlabel("x", fontsize='15', loc='right')
axs[1,1].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

# ierobezo vertibu intervalus uz asim (pietuvina grafika dalu)
axs[1,1].set_xlim((15,25))
axs[1,1].set_ylim((0.85,1.05))

#----------------------------------------------------------------------
#                                 Nt = 1000
#----------------------------------------------------------------------

# intervala [0;T] sadalijuma soļu skaits
Nt = 1000
# intervala [0;T] soļa garums
Ʈ = T / Nt
# t vērtības intervalaa [0;T]
t = np.arange(0, T + Ʈ, T/Nt)
# apreekina mainiigo gamma
γ = Ʈ / (h**2)
print("γ3=",γ)

#-------------------------------------------------------------------------------------
# ANALITIKSI APREKINI, KAD Nt = 1000
#------------------------------------------------------------------------------------
# u matricaa saglabaa analitiskas vertiibas
u_a = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas vertibas no intervala [0;L] viduspunta
videja_vertiba_a = np.zeros((Nt+1))

#analitisko vertibu aprekinasana
for j in range (0, Nt+1):
  for i in range (0,Nx):
    u_a[i,j] = np.e**(- ((np.pi**2) / (1 + η*(np.pi**2))) * t[j] ) * np.sin(np.pi*x[i])

# saglabaa matrica vertibas no intervala [0;L] viduspunta
for i in range(0, Nt+1):  
  videja_vertiba_a[i]= u_a[int(Nx/2),i]

#-------------------------------------------------------------------------------------
#TUVIANTO VERTIBU APREKINASANA KAD NT = 1000
#-------------------------------------------------------------------------------------

#IZVEIDO NULLU MATRICAS
# u matricaa tiks saglabatas apreekinaataas tuvinaatas vertiibas
u3 = np.zeros((Nx+1,Nt+1))
# matricas kur glabas alpha un beta vertibas
alpha3 = np.zeros((Nx+1,Nt+1))
beta3 = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas vertibas no intervala [0;L] viduspunta
videja_vertiba3 = np.zeros((Nt+1))
# kludu matricas
kluda3 = np.zeros((Nt+1))
kluda33 = np.zeros((Nx+1))

# saakuma nosaciijums 
u3[:,0] = np.sin(np.pi*x)
# robeznosacijumi
u3[0,0] = 0
u3[Nx,0] = 0 

#-------------------------------------------------------------------------------------
#Aprekina tuvinatas vertibas
for j in range (0,Nt):
  # aprekina alpha un beta
  for i in range(1,Nx):   
    A= γ*σ + η*(γ/Ʈ)
    B= γ*σ + η*(γ/Ʈ)
    C= 1 + 2*γ*σ + 2*η*(γ/Ʈ)
    F =((1-σ)*γ - η*(γ/Ʈ)) * u3[i-1,j] + (1 - 2*(1-σ)*γ + 2*η*(γ/Ʈ)) * u3[i,j] + ((1-σ)*γ - η*(γ/Ʈ)) * u3[i+1,j]

    alpha3[i+1,j] = B/(C-A*alpha3[i,j])
    beta3[i+1,j] = (A*beta3[i,j]+F)/(C-A*alpha3[i,j])

  for i in range(Nx-1,0,-1):
    u3[i,j+1] = alpha3[i+1,j]*u3[i+1,j+1]+beta3[i+1,j]

# aprekina kludas liimeni, kad t=Nt
for i in range(0,Nx+1):
  kluda33[i]= abs(u_a[i,Nt] - u3[i,Nt])

# saglaba matrica vertibas no intervala [0;L] viduspunta un aprekina kludas 
for i in range(0,Nt+1):  
  videja_vertiba3[i]= u3[int(Nx/2),i]
  kluda3[i]= abs(videja_vertiba_a[i] - videja_vertiba3[i])

# konstrue grafiku ar vertibam no intervala [0;L] viduspunta
axs[0,2].plot(videja_vertiba_a[:], 'r-', linewidth = '4')
axs[0,2].plot(videja_vertiba3[:], 'b--', linewidth = '3')

# kostrue liknes ar analitiskajam un tuvinaatajaam vertiibaam
axs[1,2].plot(u_a[:,0], 'r-',linewidth = '7')
for i in range(1,Nt+1,int(Nt/10)):
  axs[1,2].plot(u_a[:,i], 'k-',linewidth = '4')
  #axs[1,2].plot(u32[:,i], 'bo')
  axs[1,2].plot(u3[:,i], 'y--',linewidth = '2')

# sadala un pieskir x asiim veertiibas un iedod x un y asiim nosaukumus
axs[0,2].set_xticks(np.linspace(0, Nt, 11)) 
axs[0,2].set_xticklabels(np.linspace(0, T, 11))  
axs[0,2].set_xlabel("t", fontsize='15', loc='right')
axs[0,2].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

axs[0,2].set_xlim((999,1000.1))
axs[0,2].set_ylim((0.9125,0.9135))

axs[1,2].set_xticks(np.linspace(0, Nx, 5)) 
axs[1,2].set_xticklabels(np.linspace(0, L, 5))  
axs[1,2].set_xlabel("x", fontsize='15', loc='right')
axs[1,2].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

# ierobezo vertibu intervalus uz asim (pietuvina grafika dalu)
axs[1,2].set_xlim((15,25))
axs[1,2].set_ylim((0.85,1.05))

plt.show()

#----------------------------------------------------------------------
# TABULU IZVEIODSANA UN IZVADISANA
#----------------------------------------------------------------------
import plotly.graph_objects as go

Nt1=10
Nt2=100
Nt3=1000

# tabula ar analitiskajam un tuvinaatajaam vertiibaam, kad t=Nt
fig = go.Figure(data=[go.Table(
                      columnwidth = [50,100],
                      header=dict(values=['x', 'Analītiski iegūtā atrisinājuma vērtības','Nt=10;   γ=16','∆', 'Nt=100;  γ=1,6', '∆','Nt=1000; γ=0,16', '∆'],
                      font=dict(color='black', size=15),line_color='darkslategray',height=35),
                      cells=dict(values=[np.round(x[::int(Nx/10)],2), np.round(u_a[::int(Nx/10),Nt3],11),np.round(u1[::int(Nx/10),Nt1],11),  
                                    np.round(kluda12[::int(Nx/10)],11),  np.round(u2[::int(Nx/10),Nt2],11),
                                    np.round(kluda22[::int(Nx/10)],11), np.round(u3[::int(Nx/10),Nt3],11),
                                    np.round(kluda33[::int(Nx/10)],11) ],
                                  height=30,line_color='darkslategray',fill_color='white',
                                  font=dict(color='black', size=14)))
                     ])
fig.show()

# tabula ar vertibam no intervala [0;L] viduspunta
fig = go.Figure(data=[go.Table(
                      columnwidth = [50,100],
                      header=dict(values=['t', 'Analītiski iegūtā atrisinājuma vērtības','Nt=10;   γ=16', '∆', 'Nt=100;  γ=1,6', '∆','Nt=1000;  γ=0,16', '∆'],
                      font=dict(color='black', size=15),line_color='darkslategray',height=35),
                      cells=dict(values=[np.round(t[::int(Nt3/10)],2), np.round(videja_vertiba_a[::int(Nt3/10)],11),
                                         np.round(videja_vertiba1[::int(Nt1/10)],11),  np.round(kluda1[::int(Nt1/10)],11),  
                                         np.round(videja_vertiba2[::int(Nt2/10)],11),  np.round(kluda2[::int(Nt2/10)],11),  
                                         np.round(videja_vertiba3[::int(Nt3/10)],11), np.round(kluda3[::int(Nt3/10)],11) ],
                                  height=30,line_color='darkslategray',fill_color='white',
                                  font=dict(color='black', size=14)))
                     ])
fig.show()