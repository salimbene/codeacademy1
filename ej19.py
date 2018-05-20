#!/usr/bin/python2.7

"""
19. Hacer un pseudocodigo que imprima el mayor y el menor de una serie de cinco
numeros que vamos introduciendo por teclado.
"""

m=0
n=0
x=0
for c in range (5):
	x = int(raw_input('Ingrese nro'))
	if (x > m) and (c!=0):
		m = x
	elif (x < n) and (c!=0):
		n = x
	elif c == 0:
		m = x
		n = x

	print x,m,n
print m,n
