import argparse
import sys

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--x',type=float,default=1.0,help='Elige el primeor numero para operar')
	parser.add_argument('--y',type=float,default=1.0,help='Elige el segundo numero para operar')
	parser.add_argument('--operation',type=str,default='add',help='Elige la operacion')
	args=parser.parse_args()
	sys.stdout.write(str(calcular(args)))


def calcular(args):

	if args.operation == 'add':
		resultado = args.x+args.y
	if args.operation == 'div':
		resultado = args.x/args.y
	if args.operation == 'mul':
		resultado = args.x*args.y
	if args.operation == 'res':
		resultado = args.x-args.y
	return resultado


if __name__=='__main__':
	main()
