class Persona:

	def __init__(self):
		print('Soy la clase persona')
	def saludo(self,nombre):
		print(f'Hola que tal me llamo {nombre}')
	def estiron(self,crecimiento):
		
		print(f'He crecido {crecimiento}')

class Coche(Persona):
	def __init__(self):
		print('Soy la clase coche')
		super().__init__()

	def marca(self,marca):
		print(f'El coche es de la marca {marca}')


class Moto(Persona):
	def __init__(self):
		print('Soy la clase moto')
		super().__init__()


class Conductor(Moto,Coche):
	def __init__(self):
		print('Soy un conductor')
		super().__init__()

print(Conductor.__mro__)

conductor1=Conductor()






