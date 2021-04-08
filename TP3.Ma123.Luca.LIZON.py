# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 22:46:18 2021

@author: lucal
"""

import fonctions3 as f3

def Newton(f,fd,x0,epsilon,Nitermax):
    n=0
    xold = x0
    erreur = f(xold) - xold
    while abs(erreur)> epsilon and n<Nitermax:
        xnew = xold-(f(xold)/fd(xold))
        erreur = xnew - xold
        xold = xnew
        print(n)
        n+=1
    return xnew 

print(Newton(f3.f1,f3.f1der,-8,10,30))
