x = [1,2,3,4]
y= [3,5,32,1]
z=['a','b','c','d']

#Las lista deben tener el mismo tamaño

'''for a,b,z in zip(x,y,z):
	print(a,b,z)'''

print(list(zip(x,y,z)))#lista de tuplas
print(dict(zip(x,y)))#diccioanrio directamente


[print(i) for i in zip(x,y,z)]


try:
	print(i)
except:
	print('Traste de imprimir la variable i error tu valor no ha sido almacenado')



for i in zip(x,y,z):#Un zip con 4 tuplas
	print(i)

print(i,' En este caso i si fue almacenada')#Vemos como al variable i sigue guardando el valor
