from multiprocessing import Pool
from bs4 import BeautifulSoup
import random
import requests
import string





def random_starting_url():
	comienzo=''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
	#function for generating random numbers from sources provided by the operating system
	#'abcdefghijklmnopqrstuvwxyz'
	#choice elige aletoriamnete de entre una lista, como ponemos el fro elegira 3 veces
	url=''.join(['https://www.',comienzo,'.com'])
	return url

def get_url(url):
	resp = requests.get(url)
	soup = BeautifulSoup(resp.text,'lxml')
	return soup


def handle_links(url,link):
	if link.startswith('/'):#link[0]=='/':
		resultado= ''.join([url,link])
	else:
		resultado= link
	return resultado
def get_links(url):

	try:
		soup=get_url(url)
		body=soup.body
		links = [link.get('href') for link in body.find_all('a')]
		links = [handle_links(url,link) for link in links]
		links = [str(link.encode('ascii')) for link in links]
		return links

	except TypeError as e:
		#Cuando tratamos de utilizar una funcion en un objeto en el que no se puede
		#'hola' + 4 por ejemplo
		print(e)
		print('No hay hiperviculos en la pagina')
		return []

	except IndexError as e:
		#acceder a un indice que no existe en una lista	
		print(e)
		print('No hemos encontrado links validos')
		return []

	except AttributeError as e:
		#El objeto que he mos llamado no tiene ese tipo de funcion
		print(e)
		print('No tenemos links y hemos tratado con None')
		return []
	except Exception as e:
		print(e)
		return []


def main():
	number_links=50
	p=Pool(processes=number_links)
	parse_us=[random_starting_url() for _ in range (number_links)]
	data = p.map(get_links,[link for link in parse_us])#Recordamos en el mapeo primero la funcion y luego los datos
	data = [url for url_list in data for url in url_list]#Sacamos la url de una lsita de lisas y lo metemos en otra lista
	p.close()


	with open('urls.txt','w') as f:
		f.write(str(data))

if __name__=='__main__':
	main()
