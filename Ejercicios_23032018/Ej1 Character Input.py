# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:41:25 2018

@author: 106416
"""

"""
Ejercicio1: Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
Extras:
Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing 
"""

from datetime import datetime
formato="%d/%m/%Y"

nombre=input ("Introduce tu nombre:")
edad=int(input ("Introduce tu edad:"))
nacimiento=input ("Introduce tu fecha nacimiento (dd/mm/aaaa):" )
fechadesde=datetime.strptime(nacimiento, formato)
repeticiones=int(input("Introduce numero de repeticiones:"))
fecha_actual= datetime.now()
if fecha_actual.month>=fechadesde.month:
    if fecha_actual.month==fechadesde.month & fecha_actual.day>=fechadesde.day:
        fecha_100=(100-edad)+fecha_actual.year-1
    else :
        fecha_100=(100-edad)+fecha_actual.year             
else :
    fecha_100=(100-edad)+fecha_actual.year-1
for i in range(repeticiones):
     print ("\nCumpliras 100 años en el año", fecha_100)          