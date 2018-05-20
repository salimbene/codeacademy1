#!/usr/bin/python2.7

"""
28. Introducir un numero menor de 500 y pasarlo a numero romano.
"""

I=1
V=5
X=10
L=50
C=100
D=500
M=1000


n=int(raw_input('Ingrese nro: '))
R=""
while n > 0:
	if n >= 500:
		n-=500
		R+="D"
	elif n >= 400:
		n-=400
		R+="CD"
	elif n >= 100:
		n-=100
		R+="C"
	elif n >= 90:
		n-=90
		R+="XC"
	elif n >= 50:
		n-=50
		R+="L"
	elif n >= 40:
		n-=40
		R+="XL"
	elif n >= 10:
		n-=10
		R+="X"
	elif n >= 9:
		n-=9
		R+="IX"
	elif n >= 5:
		n-=5
		R+="V"
	elif n >= 4:
		n-=4
		R+="IV"
	elif n >= 1:
		n-=1
		R+="I"

print R
