#!/usr/bin/python2.7

"""
17. Hacer un pseudocodigo que imprima los numeros del 1 al 100. Que calcule la suma de
todos los numeros pares por un lado, y por otro, la de todos los impares. Mostrar los resultados.
"""

p=0
i=0
for n in range (1,101):
	if n % 2 == 0:
		p+=n
	else:
		i+=n
	print n,p,i
print p,i
