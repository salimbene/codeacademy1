#!/usr/bin/python2.7

"""
16. Imprimir y contar los multiplos de 3 desde la 3 hasta un numero que introducimos por teclado.
"""

c=3
d=0
n=int(raw_input("Ingrese nro:"))
while c < n:
	if c % 3 ==0:
		d+=1
		print c
	c+=1
print d
