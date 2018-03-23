# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:36:10 2018

@author: 106416
"""
"""
Ejercicio 6: Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

"Version 1 (me he complicado bastante)"
frase=str(input("Introduce una frase:"))
"Eliminar espacios"
frase_act=frase.replace(" ","")
long=len(frase_act)
mitad=int(long/2)
palindromo=1
for i in range(mitad):
    if (frase_act[i].lower()!=frase_act[long-1-i].lower()):
        palindromo=0
if (palindromo==0):
    print (frase+ " NO ES un palindromo")
else:
     print (frase+ " ES un palindromo")
     
"Version 2"
frase=str(input("Introduce una frase:"))
frase_act=frase.replace(" ","").lower()
alreves=frase_act[::-1]
if (alreves==frase_act): 
   print (frase+ " ES un palindromo") 
else:
   print (frase+ " NO ES un palindromo")