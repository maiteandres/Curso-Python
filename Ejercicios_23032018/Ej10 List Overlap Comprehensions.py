# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 17:12:49 2018

@author: 106416
"""

"""
Ejercicio 10: Take two lists, say for example these two:
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
"""
import random

a=random.sample(range(1,10),9)
b=random.sample(range(1,10),5)
print ("Lista a:", a)
print ("Lista b:", b)
lista=[]
lista=[i for i in a if i in b]
print ("La lista de numeros comunes es:", lista)