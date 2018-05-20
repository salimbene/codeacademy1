#!/usr/bin/python2.7
"""
31. Hacer un programa que nos permita introducir un numero por teclado y sobre el se realicen las siguientes operaciones:
- comprobar si es primo
- hallar su factorial
- imprimir su tabla de multiplicar
"""

def prime(n):
	
	for x in range(n-1,1,-1):
		if  (n % x == 0) and (x != 1):
			return False
	
	return True

def tabla(n):

	for x in range(1,11):
		print x,'x',n,'=',n*x

def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n=int(raw_input('Ingrese nro: '))
print('Primalidad:',prime(n))
print('Tabla:')
tabla(n)
print('Factorial',factorial(n))
