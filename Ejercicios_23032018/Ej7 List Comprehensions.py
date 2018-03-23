# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 17:01:48 2018

@author: 106416
"""
"""Ejercicio 7:  a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print ("Lista original", a)
lista=[]

"Forma larga"
for i in a:
    if i%2==0 :
        lista.append(i)

print ("Forma larga:Los numeros pares son: ", lista)

"Forma corta"
lista=[i for i in a if i%2==0]
print ("Forma corta:", lista)