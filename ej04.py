#!/usr/bin/python2.7

"""
4. Hacer un pseudocodigo que le pida al usuario un numero y luego un porcentaje. 
Luego, calcular el porcentaje indicado de ese numero y mostrarlo.
"""

a = float(raw_input("Ingrese nro: "))
b = int(raw_input("Ingrese %: "))
print "El ",b,"% de ",a," es ",(a*b)/100
