#!/usr/bin/python2.7

"""
30. Introducir dos numeros por teclado y mediante un menu, calcule su suma, su resta, su multiplicacion o su division.
"""

n1=int(raw_input('Ingrese nro: '))
n2=int(raw_input('Ingrese nro: '))

print('Elija operacion:')
print('[1] Suma:')
print('[2] Resta:')
print('[3] Division:')
print('[4] Multiplicacion:')
print('[0] Salir:')

o=int(raw_input('Ingrese nro: '))
while o != 0:
	if o == 1:
		print n1+n2
	elif o == 2:
		print n1-n2
	elif o == 3:
		print float(n1//n2)
	elif o == 4:
		print n1*n2
	o=int(raw_input('Ingrese nro: '))

