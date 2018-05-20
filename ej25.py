#!/usr/bin/python2.7

"""
25. Calcular el factorial de un numero, mediante subprogramas.
"""

def factorial(n):
	f=1
	for x in range(n,0,-1):
		f*=x
		print x,f
	return f

print factorial(int(raw_input('Ingrese nro: ')))
