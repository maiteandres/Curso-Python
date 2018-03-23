# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:15:25 2018

@author: 106416
"""

"""
Ejercicio 5:Write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
Extras:
Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


long_a=int(input("Introduce longitud lista a:"))
long_b=int(input("Introduce longitud lista b:"))
a=[]
b=[]
for i in range(long_a):
    a.append(random.randint(0,10))
for i in range(long_b):
    b.append(random.randint(0,10))
print ("La lista A generada aleatoriamente es:", a)
print ("La lista B generada aleatoriamente es:", b)
lista=[]
ya_esta=0
for i in a:
    for j in b:
        if(i==j):
            ya_esta=0
            for k in lista:
                if(i==k):
                    ya_esta=1
            if (ya_esta==0):
                lista.append(i)
print ("La lista de numeros comunes es:", lista)