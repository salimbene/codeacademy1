#!/usr/bin/python2.7
"""
34. Hacer un programa que lea 5 numeros y muestre las tablas de multiplicar de todos ellos.
"""
def tabla(n):
	for x in range(1,11):
		print x,'x',n,'=',n*x

n = [0] * 5 #peudo incialización

for i,x in enumerate(n):
	n[i]=int(raw_input('Ingrese nro: '))

for x in n:
	print tabla(x)
