from multiprocessing import Pool

def ejecutado(num):
	return num**2

if __name__=='__main__':
	p=Pool(processes=20)
	datos=p.map(ejecutado,range(21))
	datos2=p.map(ejecutado,[123,5321,213,54,1213,4132])
	p.close()
	print(datos)
	print(datos2)
