# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 09:57:54 2021

                                            Cálculo do Coeficiente de Sustentação pelo Cp

@author: Hans Herbert Schulz
"""
import numpy as np
import matplotlib.pyplot as plt
i       = complex(0,1)
#%% Cálculo do Coeficiente de Sustentação pelo Cp
U0      = 1 #Intercambiável
C       = 1
pi      = np.pi
alpha   = 4.3*pi/180 #Intercambiável

epsilon = 0.07 #Intercambiável
m       = 0.14 #Intercambiável
mu      = C/4*(i*m - epsilon)

a       = np.abs((C/4)-mu)
beta    = np.angle(C/4 - mu.conjugate())


#%%Calculo CIrcunferência

theta   = np.linspace(0, 2*pi, 200)
f       = mu + a*np.exp(i*theta)

Wc      = 2*U0*i*np.exp(i*theta)*(np.sin(alpha+beta)-np.sin(alpha-theta))
Cp      = 1-(Wc*(Wc.conjugate())/U0**2)

plt.plot(f.real,Cp) #Circunferência
plt.show()
#%% Aerofólio

Y       = f + C**2/16/f

W       = Wc/(1-C**2/16/f**2)
Cp2     = 1 - W*W.conjugate()/U0**2

plt.plot(Y.real, Y.imag,'k')#Jukowski
plt.axis('equal')
plt.show()

plt.plot(Y.real, Cp2) #Curva do Cp2
plt.ylim(max(Cp2),min(Cp2))
plt.show()
#%%Inegraçao Numerica 

corda   = Y.real.max() - Y.real.min()
Clnum   = (np.trapz(Cp2, Y.real))/C
Clex=  2 * pi * np.sqrt((1+epsilon) **2 + m**2) * np.sin(alpha+beta)

k1= -(1 - (Clex/Clnum))*100
