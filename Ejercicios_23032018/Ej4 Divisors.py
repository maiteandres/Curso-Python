# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:09:40 2018

@author: 106416
"""

"""
Ejercicio 4:Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
"""

numero=int(input ("Introduce un numero:"))
lista=[]
for i in range(1,numero+1):
    if (numero%i==0):
        lista.append(i)
print ("El numero introducido es divisible por los siguientes numeros:", lista)