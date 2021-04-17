lista =['arriba','abajo','izqueirda','derecha']

for i in range(len(lista)):
	print(i,lista[i])
print('---------------')
for i,j in enumerate(lista):
	print(i,j)

diccioanrio=dict(enumerate(lista))
print(diccioanrio)
