#!/usr/bin/python2.7

"""
1. Hacer un pseudocodigo que lea dos n umeros y muestre el resultado de su multiplicacion.

print("=Ejercicio #1=")
a = int(raw_input("Ingrese nro1: "))
b = int(raw_input("Ingrese nro2: "))
print(a*b)
"""


"""
2. Hacer un pseudocodigo que permita ingresar una frase y mostrarla en pantalla.

print("=Ejercicio #2=")
c = raw_input("Ingrese una frase: ")
print(c)
"""

"""
3. Hacer un pseudocodigo que lea 3 n umeros y muestre el promedio entre ellos.

print("=Ejercicio #3=")
a = float(raw_input("Ingrese nro1: "))
b = float(raw_input("Ingrese nro1: "))
c = float(raw_input("Ingrese nro1: "))
print "El promedio es: ",(a+b+c)/3
"""

"""
4. Hacer un pseudocodigo que le pida al usuario un n umero y luego un porcentaje.
Luego, calcular el porcentaje indicado de ese n umero y mostrarlo.

print("=Ejercicio #4=")
a = float(raw_input("Ingrese nro: "))
b = int(raw_input("Ingrese %: "))
print "El ",b,"% de ",a," es ",(a*b)/100
"""

"""
5. Hacer un pseudocodigo que lea dos n umeros y muestre el cuadrado de ambos.

print("=Ejercicio #5=")
a = int(raw_input("Ingrese nro1: "))
b = int(raw_input("Ingrese nro2: "))
print "El cuadrado de",a,"es ",a*a
print "El cuadrado de",b,"es ",b*b
"""

"""
6. Hacer un pseudocodigo que imprima los n umeros del 1 al 100.
print("=Ejercicio #6=")
for a in range(1,101):
	print a

"""

"""
7. Hacer un pseudocodigo que imprima los n umeros del 100 al 0, en orden
decreciente.

print("=Ejercicio #7=")
for a in range(100,0,-1):
	print a

"""

"""
8. Hacer un pseudocodigo que imprima los n umeros pares entre 0 y 100.

print("=Ejercicio #8=")
for a in range(0,100,2):
	print a
"""

"""
9. Hacer un programa que imprima la suma de los n umeros del 1 al 100.

print("=Ejercicio #9=")
b = 0
for a in range(1,101):
	b = b + a
	print a,b
"""

"""
10. Hacer un pseudocodigo que imprima los n umeros impares hasta el 100 y que
imprima cuantos impares hay.


b = 0
for a in range(1,101):
	if a % 2 ==0:
		b += 1
		print a,b
"""

"""
11. Hacer un pseudocodigo que imprima todos los n umeros naturales que hay desde la unidad hasta un n umero que introducimos por teclado.

a=1
n = int(raw_input('Ingrese un nro:'))
while (a <= n):
	print a
	a+=1
"""

"""
12. Introducir tantas frases como queramos y contarlas.
a=1
f="hola"
while (f != ""):
	f = raw_input('Ingrese una frase:')
	if f !="":
		a+=1
print a
"""

"""
13. Hacer un pseudocodigo que solo nos permita introducir S o N.
n=""
while (n != 'S') and (n != 'N'):
	n = raw_input('Ingrese N o S')

print "Ok"
"""

"""
14. Introducir un n umero por teclado y que el algoritmo nos diga si es positivo o
negativo.

n=int(raw_input("Ingrese nro:"))
if n > 0:
	print "Es positivo"
else:
	print "Es negativo"
"""

"""
15. Introducir un n umero por teclado y que el algoritmo nos diga si es par o impar.

n = int(raw_input("Ingrese nro:"))
if n % 2 == 0:
	print "PAR"
else:
	print "INPAR"
"""

"""
16. Imprimir y contar los m ultiplos de 3 desde la 3 hasta un n umero que
introducimos por teclado.
c=3
d=0
n=int(raw_input("Ingrese nro:"))
while c < n:
	if c % 3 ==0:
		d+=1
		print c
	c+=1
print d
"""

"""
17. Hacer un pseudocodigo que imprima los n umeros del 1 al 100. Que calcule la
suma de todos los n umeros pares por un lado, y por otro, la de todos los
impares. Mostrar los resultados.
p=0
i=0
for n in range (1,101):
	if n % 2 == 0:
		p+=n
	else:
		i+=n
	print n,p,i
print p,i
"""

"""
18. Imprimir y contar los n umeros que son m ultiplos de 2 o de 3 que hay entre 1 y
100.
p=0
for n in range (1,101):
	if (n % 2 == 0) or (n % 3 == 0):
		p+=1
		print n
print p
"""

"""
19. Hacer un pseudocodigo que imprima el mayor y el menor de una serie de cinco
n umeros que vamos introduciendo por teclado.
m=0
n=0
x=0
for c in range (5):
	x = int(raw_input('Ingrese nro'))
	if (x > m) and (c!=0):
		m = x
	elif (x < n) and (c!=0):
		n = x
	elif c == 0:
		m = x
		n = x

	print x,m,n
print m,n
"""

"""
20. Introducir dos n umeros por teclado. Imprimir los n umeros naturales que hay
entre ambos n umeros empezando por el mas pequeno, contar cuantos hay y
cuantos de ellos son pares. Calcular la suma de los impares.

a=int(raw_input('Ingrese nro1: '))
b=int(raw_input('Ingrese nro2: '))
c=0
p=0
i=0

for x in range(a,b+1):
	if x >= 0:
		c+=1
		if x % 2 == 0:
			p+=1
		else:
			i+=x
	print x
print c,p,i
"""

"""
21. Imprimir diez veces la serie de n umeros del 1 al 10.

for x in range (1,11):
	for y in range(1,11):
		print x,y
"""

"""
22. Imprimir, contar y sumar los m ultiplos de 2 que hay entre un par de
N umeros a ingresar, tal que el segundo sea mayor o igual que el primero.

c=0
s=0
a=int(raw_input('Ingrese nro1: '))
b=int(raw_input('Ingrese nro2: '))

while b < a:
	b=int(raw_input('Ingrese nro2: '))

for x in range(a,b):
	if x % 2 == 0:
		c+=1
		s+=x
		print x,c,s
"""

"""
23. Hacer un pseudocodigo que cuente las veces que aparece una determinada
letra en una frase que introduciremos por teclado.

c=0
f=raw_input('Ingrese frase:')
l=raw_input('Ingrese letra:')

print f.count(l)

for x in f:
	if x == l:
		c+=1

print c
"""

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
"""

"""
25. Calcular el factorial de un n umero, mediante subprogramas.

def factorial(n):
	f=1
	for x in range(n,0,-1):
		f*=x
		print x,f
	return f

print factorial(int(raw_input('Ingrese nro: ')))
"""

"""
26. Hacer un programa que calcule independientemente la suma de los m ultiplos de
5 y de los m ultiplos de 10, de los n umeros entre 1 y 1000.

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

"""

"""
27. Comprobar si un n umero mayor o igual que 1 es primo.
https://en.wikipedia.org/wiki/Primality_test
	print(prime(int(raw_input('Ingrese nro1: '))))


def prime(n):
	
	for x in range(n-1,1,-1):
		if  (n % x == 0) and (x != 1):
			return False
	
	return True

for x in range(30):
	print(x,prime(x))
"""

"""
28. Introducir un n umero menor de 500 y pasarlo a numero romano.
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
"""	

"""
29. Realizar la tabla de multiplicar de un numero entre 0 y 10.


n=int(raw_input('Ingrese nro: '))
for x in range(1,11):
	print x,'x',n,'=',n*x
"""

"""
30. Introducir dos n umeros por teclado y mediante un menu, calcule su suma, su resta, su multiplicacion o su division.

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

"""

"""

31. Hacer un programa que nos permita introducir un numero por teclado y sobre el se realicen las siguientes operaciones:
- comprobar si es primo
- hallar su factorial
- imprimir su tabla de multiplicar



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
"""



"""
32. Crear un array de 20 elementos con nombres de personas. Visualizar los elementos de la lista.

n = ['Jorge','Carlos','Pedro','Matias','Martin','Vicky','Eugenia','Maria','Cecilia','Carolina','Dario','Leonardo','Natalia','Jose','Pablo','Juliana','Fernanda','Marina','Damian','Guido']

for x in n:
	print(x)
"""

"""
#!/usr/bin/python2.7

33. Hacer un programa que lea las calificaciones de un alumno en 10 asignaturas, las almacene en un vector y calcule e imprima su promedio.

n = [0] * 10
p=0

for x in n:
	x =int(raw_input('Ingrese nota'))
	p+=x

print p/len(n)
"""


"""
34. Hacer un programa que lea 5 numeros y muestre las tablas de multiplicar de todos ellos.

def tabla(n):

	for x in range(1,11):
		print x,'x',n,'=',n*x


n = [0] * 5

for i,x in enumerate(n):
	n[i]=int(raw_input('Ingrese nro: '))

for x in n:
	print tabla(x)

"""
