
"""
26. Hacer un programa que calcule independientemente la suma de los multiplos de 5 y 
de los multiplos de 10, de los numeros entre 1 y 1000.
"""

m5=0
m10=0
for x in range(1,1001):
	if x % 10 == 0:
		m10+=x
		if x % 5 == 0:
			m5+=x
	elif x % 5 == 0:
		m5+=x

	print x,m5,m10

