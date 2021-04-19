import multiprocessing

def spawn(num):
	print(f'Spawned! {num}')


#Esto solo funciona cuando se ejecuta el script como tal , una llamada a este codigo desde otro script no lo ejecutaria
if __name__=='__main__':
	for i in range(55):
		p =multiprocessing.Process(target=spawn,args=(i,))
		p.start()
		#p.join()#Sirve para esperar un tiempo entre procesos
		#Los procesos de esta manera estan conectados y pueden intercambiar variables entre ellos
		#sin embargo tardaran mas
