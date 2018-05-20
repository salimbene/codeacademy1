#!/usr/bin/python2.7

"""
29. Realizar la tabla de multiplicar de un numero entre 0 y 10.
"""

n=int(raw_input('Ingrese nro: '))
for x in range(1,11):
	print x,'x',n,'=',n*x
