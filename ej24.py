#!/usr/bin/python2.7

"""
24. Hacer un pseudocodigo que simule el funcionamiento de un reloj digital y
que permita ponerlo en hora.

h=int(raw_input('Ingrese Horas: '))
m=int(raw_input('Ingrese Minutos: '))
s=int(raw_input('Ingrese Segundos: '))

for x in range(h,24):
	for y in range(m,60):
		for z in range(s,60):
			print x,y,z
		s=0
	m=0
