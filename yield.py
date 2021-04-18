#Recordamos qeu los valores de los generadores no se alamcenan en la memoria
#Una vez utilizados se desechan
#Calculan un numero y van al siguiente

def generador():
	yield 'OH'
	yield 'Hello'
	yield 'Hey'

for i in generador():
	print(i)

correct_combo=(3,6,7)
#Manera incorreta uso inecesario de la memoria
def generador():
	for c1 in range(10):
		for c2 in range(10):
			for c3 in range(10):
				yield (c1,c2,c3)#Yield actua como generador , el cual guarda las ordenes en un espacio en
				                #la memoria pero no lo ejecuta
				                #Yield es como poner return solo que devolvera un generador
for (c1,c2,c3) in generador():
	print(c1,c2,c3)
	if (c1,c2,c3) == correct_combo:
		print('Correct')
		break
	print(c1,c2,c3)
				
'''

def generador():
	for c1 in range(10):
		for c2 in range(10):
			for c3 in range(10):
				yield (c1,c2,c3)

En este caso la funcion generador cuando la llamemos ejectura el codigo hasta que llegue a yield
Entonces actuara como generador y devolvera el primer valor que sera (0,0,0)
Si la llamamos otra vez ese valor ya no volvera y no esta almacenado en la memoria, como podria ser en el ejemplo de una lista
Cuando volvamos a llamar a la funcion generador() esta recordara el anterior recorrdio que hizo que fue (0,0,0)
He ira a por el siguiente (0,0,1), asi hasta que no llamemos mas a la funcion o recorramos todos los for
Esta es una manera de ahorrar espacio en memoria , ya que se van ejecutando las ordenes en el momento y no se gaurdan.



'''
