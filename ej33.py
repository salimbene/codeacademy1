#!/usr/bin/python2.7
"""
33. Hacer un programa que lea las calificaciones de un alumno en 10 asignaturas, las almacene en un vector y
calcule e imprima su promedio.
"""
n = [0] * 10
p=0

for x in n:
	x =int(raw_input('Ingrese nota'))
	p+=x

print p/len(n)
