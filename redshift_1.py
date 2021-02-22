#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 19:53:24 2021

@author: Saadia Bayou
"""

"""" Ce programme calcul le décalage de raie spectrale 
     entre la longeur d'onde émise et la longueur d'onde observée,
     lors du rayonnement d'un objet astrophysique telle qu'une galaxie  """

# Données :     

data1=["lambda obs","lambda em"]
data2=["lambda em","lambda obs"]

data3=["lambda em","z"]
data4=["z","lambda em"]

data5=["lambda obs","z"]
data6=["z","lambda obs"]

# Données
evJ=1.6076634e-19 # Joules -> 1 electronvolt vaut 1,6076634.10e-19 Joules
RH=1.10e7 # RH = 1.10e7 m-1
h=6.63e-34 # h = 6.63e-34 m2.kg.s-1
c=3.00e8 # c=3.00e08 m.s-1  

# Définition des fonction de calculs :

def raie_H(n1,n2):
    """ Calcul de la longuer d'onde"""    
    return 1/(RH*((1/(n1**2))-(1/(n2**2))))

# Calcul redshift z    
def redshift_z(lo,le):
    return (lo/le)-1

# Calcul de lambda observée 
def calcul_lamb_obs(z,le):
    # formule :
    return (z+1)*le 

# Calcul de lambda emise
def calcul_lamb_em(z,lo):
    # formule :
    return lo/(z+1)

data=[]
print(" \nQuelles sont les deux données connues ?\n ")
print(" \nEntrer lambda obs pour -> longeur d'onde observée\n")
print(" \nEntrer lambda em pour -> longeur d'onde émise\n")
print(" \nEntrer z pour -> la valeur du redshift z \n")


for i in range(2):
    print("\ndonnée n°",i+1)
    d=input("Entrer nom de la donnée : ")
    data.append(d)

print("\ndata =",data)

print("\nLes valeurs connues sont : ", data)


if data==data1 or data==data2 :
    print("\nz -> donnée inconnue :\n ")
    
    print("\nDétermination du décalage spectrale  z :\n ")
    
    print("Etape 1 - calcul de lambda emise :")
#
    n1=int(input("Entrer la valeur du niveau initial : n1 = "))
    n2=int(input("Entrer la valeur du niveau final: n2 = "))

    lambda_em=raie_H(n1,n2)
    
    print("\nlambda emise = ",lambda_em, "m")
    
    lambda_obs=float(input("Entrer la valeur de la longueur d'onde observée en mètre : "))
    
    print("\nlambda observée = ",lambda_obs)
    
    print("\nEtape 2 - calcul de la valeur de z :")
    
    z=redshift_z(lambda_obs,lambda_em)
    print("\nredshift z= ", z)
    

# Cas 2 - Calcul lambda obs
elif data==data3 or data==data4 :
    print("\n lambda observée ->  donnée inconnue :\n ")
    
    print("\nDétermination de lambda observée :\n ")
    
    print("Etape 1 - calcul de lambda emise :")
    
    n1=int(input("Entrer la valeur du niveau initial : n1 = "))
    n2=int(input("Entrer la valeur du niveau final: n2 = "))
    
    lambda_em=raie_H(n1,n2)
    
    print("\nlambda emise = ",lambda_em, "m")
    
    z=float(input("Entrer la valeur de z : "))
    
    print("\nz = ",z)
    
    print("\nEtape 2 - calcul de la valeur de la longueur d'onde observée :")
    
    lambda_obs=calcul_lamb_obs(z,lambda_em)
    print("\nlambda observée = ", lambda_obs)

# Cas 3 - Calcul lambda em    
elif data==data5 or data==data6:
    print("\n lambda emise ->  donnée inconnue :\n ")
    
    print("\nDétermination de lambda émise :\n ")

    
    z=float(input("Entrer la valeur de z : "))
    lambda_obs=float(input("Entrer la valeur de la longueur d'onde observée en mètre : "))
    
    print("\nz = ",z)
    print("\nlambda observée = ",lambda_obs)
    
# Appel de la fonction calcul_lamb_em 
    lambda_em=calcul_lamb_em(z,lambda_obs)
    print("\nlambda emise = ",lambda_em)
    
# Cas 4 - erreur de saisie
else: "Saisie des données d'entrées érronée"
  
 
    
