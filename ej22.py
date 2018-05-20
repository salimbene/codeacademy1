#!/usr/bin/python2.7

"""
22. Imprimir, contar y sumar los multiplos de 2 que hay entre un par de
Numeros a ingresar, tal que el segundo sea mayor o igual que el primero.
"""

c=0
s=0
a=int(raw_input('Ingrese nro1: '))
b=int(raw_input('Ingrese nro2: '))

while b < a:
	b=int(raw_input('Ingrese nro2: '))

for x in range(a,b):
	if x % 2 == 0:
		c+=1
		s+=x
		print x,c,s
