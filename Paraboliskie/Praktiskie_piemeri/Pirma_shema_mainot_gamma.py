import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))
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

#----------------------------------------------------------------------
#                               Nt = 100
#----------------------------------------------------------------------
# intervala [0;T] sadalijuma soļu skaits
Nt = 100
# intervala [0;T] soļa garums
Ʈ = T / Nt
# t vērtības intervalaa [0;T]
t = np.arange(0, T + Ʈ, T/Nt)
γ = Ʈ / (h**2)
# apreekina mainiigo gamma
print("γ1=",γ)
#-------------------------------------------------------------------------------------
# ANALITIKSI APREKINI, KAD Nt = 100
#------------------------------------------------------------------------------------
# u matricaa saglabaa analitiskas vertiibas
u_a = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas vertibas no intervala [0;L] viduspunta
videja_vertiba_a = np.zeros((Nt+1))

#analitisko vertibu aprekinasana
for j in range (0, Nt+1):
  for i in range (1,Nx):
    u_a[i,j] = np.e**(-(np.pi**2)*t[j] ) * np.sin(np.pi*x[i])

# saglaba matrica vertibas no intervala [0;L] viduspunta
for i in range(0,Nt+1):  
  videja_vertiba_a[i]= u_a[int(Nx/2),i]

#-------------------------------------------------------------------------------------
#TUVIANTO VERTIBU APREKINASANA KAD NT = 100
#-------------------------------------------------------------------------------------

#IZVEIDO NULLU MATRICAS
# u matricaa tiks saglabatas apreekinaataas tuvinaatas vertiibas
u1 = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas vertibas no intervala [0;L] viduspunta
videja_vertiba1 = np.zeros((Nt+1))
# kludu matricas
kluda1=np.zeros(Nt+1)
kluda11=np.zeros(Nx+1)

# saakuma nosaciijums 
u1[:,0] = np.sin(np.pi*x)
# robeznosacijumi
u1[0,0] = 0
u1[Nx,0] = 0 

#-------------------------------------------------------------------------------------
#Aprekina tuvinatas vertibas
for j in range(0,Nt):
  for i in range(1, Nx):
      u1[i,j+1] = γ * (u1[i+1,j] - 2 * u1[i,j] + u1[i-1,j]) + u1[i,j]

# saglaba matrica vertibas no intervala [0;L] viduspunta un aprekina kludas 
for i in range(0,Nt+1):  
  videja_vertiba1[i]= u1[int(Nx/2),i]
  kluda1[i] = abs(videja_vertiba_a[i] - videja_vertiba1[i])

# aprekina kludas liimeni, kad t=Nt
for i in range(0,Nx+1):
   kluda11[i]= abs(u_a[i,Nt] - u1[i,Nt])

# kostrue liknes ar analitiskajam un tuvinaatajaam vertiibaam, kad t=Nt
axs[0,0].plot(u_a[:,Nt], 'r-', linewidth='4')
axs[0,0].plot(u1[:,Nt], 'b--', linewidth='3')

# konstrue grafiku ar vertibam no intervala [0;L] viduspunta
axs[1,0].plot(videja_vertiba_a[:], 'r-', linewidth='4')
axs[1,0].plot(videja_vertiba1[:], 'b--', linewidth='3')

# sadala un pieskir x asiim veertiibas un iedod x un y asiim nosaukumus
axs[0,0].set_xticks(np.linspace(0, Nx, 5)) 
axs[0,0].set_xticklabels(np.linspace(0, L, 5))  
axs[0,0].set_xlabel("x", fontsize='15', loc='right')
axs[0,0].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

axs[1,0].set_xticks(np.linspace(0, Nt, 11)) 
axs[1,0].set_xticklabels(np.linspace(0, T, 11))  
axs[1,0].set_xlabel("t", fontsize='15', loc='right')
axs[1,0].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

#----------------------------------------------------------------------
#                               Nt = 1000
#----------------------------------------------------------------------

# intervala [0;T] sadalijuma soļu skaits
Nt = 1000
# intervala [0;T] soļa garums
Ʈ = T / Nt
# t vērtības intervalaa [0;T]
t = np.arange(0, T + Ʈ, T/Nt)
# apreekina mainiigo gamma
γ = Ʈ / (h**2)
print("γ=",γ)

#-------------------------------------------------------------------------------------
# ANALITIKSI APREKINI, KAD Nt = 1000
#------------------------------------------------------------------------------------

# u matricaa saglabaa analitiskas vertiibas
u_a = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas vertibas no intervala [0;L] viduspunta
videja_vertiba_a = np.zeros((Nt+1))

#analitisko vertibu aprekinasana
for j in range (0, Nt+1):
  for i in range (1,Nx):
    u_a[i,j] = np.e**(-(np.pi**2)*t[j] ) * np.sin(np.pi*x[i])

# saglabaa matrica vertibas no intervala [0;L] viduspunta
for i in range(0,Nt+1):  
  videja_vertiba_a[i]= u_a[int(Nx/2),i]

#-------------------------------------------------------------------------------------
#TUVIANTO VERTIBU APREKINASANA KAD Nt = 1000
#-------------------------------------------------------------------------------------

#IZVEIDO NULLU MATRICAS
# u matricaa tiks saglabatas apreekinaataas tuvinaatas vertiibas
u2 = np.zeros((Nx+1,Nt+1))
# videja_vertiba matrica ,kura tiks saglabatas vertibas no intervala [0;L] viduspunta
videja_vertiba2 = np.zeros((Nt+1))
# kludu matricas
kluda2=np.zeros(Nt+1)
kluda22=np.zeros(Nx+1)

# saakuma nosaciijums 
u2[:,0] = np.sin(np.pi*x)
# robeznosacijumi
u2[0,0] = 0
u2[Nx,0] = 0 

#-------------------------------------------------------------------------------------
#Aprekina tuvinatas vertibas
for j in range(0,Nt):
  for i in range(1, Nx):
      u2[i,j+1] = γ * (u2[i+1,j] - 2 * u2[i,j] + u2[i-1,j]) + u2[i,j]

# saglaba matrica vertibas no intervala [0;L] viduspunta un aprekina kludas 
for i in range(0,Nt+1):  
  videja_vertiba2[i]= u2[int(Nx/2),i]
  kluda2[i] = abs(videja_vertiba_a[i] - videja_vertiba2[i])

# aprekina kludas liimeni, kad t=Nt
for i in range(0,Nx+1):
   kluda22[i]= abs(u_a[i,Nt] - u2[i,Nt])

# kostrue liknes ar analitiskajam un tuvinaatajaam vertiibaam, kad t=Nt
axs[0,1].plot(u_a[:,Nt], 'r-', linewidth='4')
axs[0,1].plot(u2[:,Nt], 'b--', linewidth='3')

# konstrue grafiku ar vertibam no intervala [0;L] viduspunta
axs[1,1].plot(videja_vertiba_a[:], 'r-', linewidth='4')
axs[1,1].plot(videja_vertiba2[:], 'b--', linewidth='3')

# sadala un pieskir x asiim veertiibas un iedod x un y asiim nosaukumus
axs[0,1].set_xticks(np.linspace(0, Nx, 5)) 
axs[0,1].set_xticklabels(np.linspace(0, L, 5))  
axs[0,1].set_xlabel("x", fontsize='15', loc='right')
axs[0,1].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

axs[1,1].set_xticks(np.linspace(0, Nt, 11)) 
axs[1,1].set_xticklabels(np.linspace(0, T, 11))  
axs[1,1].set_xlabel("t", fontsize='15', loc='right')
axs[1,1].set_ylabel("u(x,t)", fontsize='15', rotation=0, loc='top')

plt.show()

#----------------------------------------------------------------------
# TABULU IZVEIODSANA UN IZVADISANA
#----------------------------------------------------------------------
import plotly.graph_objects as go

Nt1=100
Nt2=1000

# tabula ar vertibam no intervala [0;L] viduspunta
fig = go.Figure(data=[go.Table(
                      columnwidth = [20,40,60,60,50,50],
                      header=dict(values=['t','Analītiski iegūtās atrisinājuma vērtības','Nx=40;  Nt=100;                γ=1,6', '∆1','Nx=40;  Nt=1000;     γ=0,16','∆2'],
                      font=dict(color='black', size=15),line_color='darkslategray', height=35),
                      cells=dict(values=
                                 [np.round(t[::int(Nt/10)],2), 
                                  np.round(videja_vertiba_a[::int(Nt2/10)],9), np.round(videja_vertiba1[::int(Nt1/10)],9),np.round(kluda1[::int(Nt1/10)],9),  
                                  np.round(videja_vertiba2[::int(Nt2/10)],9),np.round(kluda2[::int(Nt2/10)],9)
                                 ],
                      height=30,line_color='darkslategray',fill_color='white', font=dict(color='black', size=14)
                                  ))
                     ])
fig.show()

# tabula ar analitiskajam un tuvinaatajaam vertiibaam, kad t=Nt
fig = go.Figure(data=[go.Table(
                      columnwidth = [20,40,60,60,50,60],
                      header=dict(values=['x','Analītiski iegūtās atrisinājuma vērtības','Nx=40;  Nt=100;                γ=1,6', '∆1','Nx=40;  Nt=1000;     γ=0,16','∆2'],
                      font=dict(color='black', size=15),line_color='darkslategray', height=35),                      
                      cells=dict(values=
                                 [np.round(x[::int(Nx/10)],2), 
                                  np.round(u_a[::int(Nx/10),Nt2],9), np.round(u1[::int(Nx/10),Nt1],9),np.round(kluda11[::int(Nx/10)],10),
                                  np.round(u2[::int(Nx/10),Nt2],9),np.round(kluda22[::int(Nx/10)],20)
                                 ],
                      height=30,line_color='darkslategray',fill_color='white', font=dict(color='black', size=15)
                                  ))
                     ])
fig.show()