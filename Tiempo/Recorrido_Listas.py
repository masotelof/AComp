import matplotlib.pyplot as plt
from random import random
from time import time

if __name__ == "__main__":
	# número de ejecuciones
	iteraciones = 31
	# número de iteraciones máximas
	max_elem  = 1000000
	# particiones
	par = 100
	size = max_elem/par

	# Diferentes tamaños para probar
	num_elem = [ int(size*i) for i in range(1,par+1)]
	time_pos =[]
	time_it =[]
	time_fn =[]
	
	for tam in num_elem:
		
		# elementos con los que se van a probar
		elementos = [random() for _ in range(tam)]
		
		prom=0
		for _ in range(iteraciones):
			tini = time()
			suma = 0
			for i in range(len(elementos)):
				suma += elementos[i]
			tfin = time()
			prom += tfin-tini
		time_pos.append(prom/iteraciones)
		
		
		prom=0
		for _ in range(iteraciones):
			tini = time()
			suma = 0
			for elemento in elementos:
				suma += elemento
			tfin = time()
			prom += tfin-tini
		time_it.append(prom/iteraciones)
		
		prom=0
		for _ in range(iteraciones):
			tini = time()
			suma = sum(elementos)
			tfin = time()
			prom += tfin-tini
		time_fn.append(prom/iteraciones)
	
	# graficamos los resultados
	plt.plot(num_elem, time_pos, label="Posición")
	plt.plot(num_elem, time_it, label="Iterador")
	plt.plot(num_elem, time_fn, label="Función")
	plt.title("Tiempo de Ejecución para la Suma de una Lista de Elementos")
	plt.xlabel("Número de Elementos")
	plt.ylabel("Tiempo")
	plt.legend(loc="upper left")
	plt.show()
