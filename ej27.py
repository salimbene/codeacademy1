
"""
27. Comprobar si un numero mayor o igual que 1 es primo.
https://en.wikipedia.org/wiki/Primality_test
"""

print(prime(int(raw_input('Ingrese nro1: '))))


def prime(n):
	
	for x in range(n-1,1,-1):
		if  (n % x == 0) and (x != 1):
			return False
	
	return True

for x in range(30):
	print(x,prime(x))

