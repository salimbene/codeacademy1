#!/usr/bin/python2.7

"""
20. Introducir dos numeros por teclado. Imprimir los numeros naturales que hay
entre ambos numeros empezando por el mas pequeño, contar cuantos hay y
cuantos de ellos son pares. Calcular la suma de los impares.
"""

a=int(raw_input('Ingrese nro1: '))
b=int(raw_input('Ingrese nro2: '))
c=0
p=0
i=0

for x in range(a,b+1):
	if x >= 0:
		c+=1
		if x % 2 == 0:
			p+=1
		else:
			i+=x
	print x
print c,p,i
