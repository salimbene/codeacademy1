#!/usr/bin/python2.7

"""
10. Hacer un pseudocodigo que imprima los numeros impares hasta el 100 y que imprima cuantos impares hay.
"""

b = 0
for a in range(1,101):
	if a % 2 ==0:
		b += 1
		print a,b
