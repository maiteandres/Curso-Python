# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 17:22:53 2018

@author: 106416
"""
"""Ejercicio 8: Make a two-player Rock-Paper-Scissors game"""

def funcion (resp_1, resp_2):
    if (resp_1==resp_2):
        respuesta=(" Habeis empatado")
    elif resp_1=="piedra":
        if resp_2=="tijera":
             respuesta=(" Ha ganado el jugador 1")
        else:
            respuesta=(" Ha ganado el jugador 2")
    elif resp_1=="tijera":    
         if resp_2=="piedra":
             respuesta=(" Ha ganado el jugador 2")
         else:
            respuesta=(" Ha ganado el jugador 1")
    elif resp_1=="papel":    
         if resp_2=="piedra":
            respuesta=(" Ha ganado el jugador 1")
         else:
           respuesta=(" Ha ganado el jugador 2")
    else:
       respuesta=(" Las opciones elegidas no son válidas") 
    return (respuesta)        


Seguir=1
Nombre1=str(input ("Introduce su nombre:"))
while (Seguir==1):
     Jugador1=input ("%s, Introduce piedra papel o tijera:" %Nombre1)   
     Jugador2=input ("Jugador 2: Introduce piedra papel o tijera:")   
     respuesta=funcion(Jugador1.lower(), Jugador2.lower())
     print(respuesta)
     Seguir=int(input ("Quiere seguir jugando? (1/0):"))  