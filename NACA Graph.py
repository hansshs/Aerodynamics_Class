# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 11:28:35 2021

@author: Hans Herbert 
"""
import numpy as np
import matplotlib.pyplot as plt
#%%NACA Upper Airfoil Profile
def UpperProfile(M,P,Z,W):
    p=P/10
    m=M/100
    
    x= np.linspace(0,p,10)
    y= np.linspace(p,1,10)
    
    z1=(m/(p**2))*(2*p*x-(x**2))
    z2=(m/((p-1)**2))*(2*p*y-y**2+(1-2*p))
    plt.plot(x,z1, 'r')
    plt.plot(y,z2, 'b')
    plt.xlim(0, 1)
    plt.ylim(0, 0.1)
    plt.ylabel("Zc")
    plt.xlabel("Wing Length(%)")
    plt.title("NACA "+str(M)+str(P)+str(Z)+str(W)+ " Airfoil Upper Profile")
    plt.show()
