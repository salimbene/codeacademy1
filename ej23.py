#!/usr/bin/python2.7
"""
23. Hacer un pseudocodigo que cuente las veces que aparece una determinada letra en una frase que introduciremos por teclado.


Notar que está resuelto de dos maneras, ya que python tiene una función que realiza lo que pide la consiga -count-
También esta resuelto con un loop para mostar una manera lógica de resolverlo

"""

c=0
f=raw_input('Ingrese frase:')
l=raw_input('Ingrese letra:')

print f.count(l)

for x in f:
	if x == l:
		c+=1

print c
