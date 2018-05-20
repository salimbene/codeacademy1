#!/usr/bin/python2.7

"""
12. Introducir tantas frases como queramos y contarlas.
"""

a=1
f="hola"
while (f != ""):
	f = raw_input('Ingrese una frase:')
	if f !="":
		a+=1
print a
