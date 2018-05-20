#!/usr/bin/python2.7

"""
18. Imprimir y contar los n umeros que son m ultiplos de 2 o de 3 que hay entre 1 y 100.
"""

p=0
for n in range (1,101):
	if (n % 2 == 0) or (n % 3 == 0):
		p+=1
		print n
print p
