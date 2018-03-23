# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:57:32 2018

@author: 106416
"""
"""
Ejercicio 3: Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
Extras:
Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
"""



"Version 1"
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("Version 1\nLos numeros mayores de 5 son:")
for i in a:
    if i<5:
        print(a[i])
        
        
"Version 2"
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lista=[]
print("Version 2\nLos numeros mayores de 5 son:")
for i in a:
    if i<5:
        lista.append(i)
print(lista)

"Version 3"
numero=int(input("Introduce un numero:"))
lista=[]
print("Version 3\nLos numeros mayores de ", numero, "son:")
for i in a:
    if i<numero:
        lista.append(i)
print(lista)