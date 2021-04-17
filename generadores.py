#generador tiempo
#lista memoria

#normal
lista3=[]
for i in range(5):
	lista3.append(i)
print(lista3)

#comprimido
lista = [i for i in range(5)]
print(lista)

#generador
lista2 = (i for i in range(5))
print(lista2)


lista_ejemplo =[5,5,31,2,123,30,90,80,214,324,23,43,12,54,32,34,35]

def div_five(num):
	if num % 5 == 0:
		resultado = True
	else:
		resultado= False

	return resultado

xyz = (i for i in lista_ejemplo if div_five(i))

'''xyz = []

for i in lista_ejemplo:
	if div_five(i):
		xyz.append(i)'''


[print(i) for i in xyz]#list comprenhension
#(print(i) for i in xyz)#generator


[[print(i,ii) for ii in range(5)]for i in range(5)]

for i in range(5):
	for ii in range(5):
		print(i,ii)

xyz =[[print[i,ii] for ii in range(5)]for i in range(5)]

for i in xyz:
	i
