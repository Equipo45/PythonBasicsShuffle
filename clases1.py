class Persona:
	def __init__(self,nombre,estatura):

		self.nombre=nombre
		self.estatura=estatura

	def saludo(self):
		print(f'Hola que tal me llamo {self.nombre}')
	def estiron(self,crecimiento):
		self.estatura+= crecimiento

Eduardo = Persona('Eduardo',170)

print(Eduardo.estatura)
Eduardo.estiron(10)
print(Eduardo.estatura)




