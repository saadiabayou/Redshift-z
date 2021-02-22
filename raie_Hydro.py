#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 19:47:10 2021

@author: Saadia Bayou
"""

""" Programme raie_Hydro : calcul de la longueur d'onde """

# Données
evJ=1.6076634e-19 # Joules -> 1 electronvolt vaut 1,6076634.10e-19 Joules
RH=1.10e7 # RH = 1.10e7 m-1
h=6.63e-34 # h = 6.63e-34 m2.kg.s-1
c=3.00e8 # c=3.00e08 m.s-1  
#lambdas=[]
#Energies=[]

n1=int(input("Entrer la valeur du niveau initial : n1 = "))
n2=int(input("Entrer la valeur du niveau final: n2 = "))

def raie_H(n1,n2):
    """ Calcul de la longuer d'onde"""    
    return 1/(RH*((1/(n1**2))-(1/(n2**2))))

raie_H(n1,n2)