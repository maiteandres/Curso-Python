# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:18:15 2018

@author: 106416
"""
"""
Ejercicio 2: Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user
"""

numero=int(input ("Introduce un numero:"))
if numero%2==0:
    if numero%4==0:
        print ("El numero además de ser par es multiplo de 4")
    else:
        print ("El numero es par pero no multiplo de 4")
else:
    print ("El numero es impar")
num=int(input ("Introduce divisor:"))
check=int(input ("Introduce dividendo:"))
if check%num==0:
     print ("El resultado de la división es", check/num)
else:
      print ("Los numeros introducidos no son divisibles")