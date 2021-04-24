def funcion(*args):
	for arg in args:
		print(arg)

def funcion(**kwargs):
	for key, value in kwargs.items():
		print(key,value)

def funcion(*args,**kwargs):
	for key, value in kwargs.items():
		print(key,value)
	for arg in args:
		print(arg)




def funcion_suma(x,y):
	resultado=x+y
	print(resultado)

lista=[2,3]

funcion_suma(*lista)
print(*lista)

#otra manera de hacerlo
def funcion_suma(*numeros):
	resultado=0
	for numero in numeros:
		resultado+=numero
	print(resultado)

lista=[2,3]

funcion_suma(*lista)

