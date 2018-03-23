# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 17:56:15 2018

@author: 106416
"""

"""Ejercicio 9: Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""
import random

salir=0
while(salir==0):
    numero_generado=random.randint(1,9)
    adivinado=0
    contador=0
    while(adivinado==0 and salir==0):
       respuesta=input("Introduzca un numero o exit para salir:")
       if(respuesta=="exit"):
           salir=1 
       else:
           numero_respondido=int(respuesta)
           contador=contador+1
           if numero_respondido<numero_generado:
               print ("El número es más alto")
           elif numero_respondido>numero_generado:
                print ("El número es más bajo")
           else:
                print ("Has acertado a la ",contador)
                adivinado=1
                  
print ("Fin del juego") 
