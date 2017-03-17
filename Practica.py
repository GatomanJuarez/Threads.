"""Se va a crear dos hilos
 Funcion:
	Numero random
	Capturar ese numero
	Se termina el proceso (hilo)
"""

import threading
import time
import random
import os
import logging

def PrimerH(Hilo):
	salida = False
	while salida == False:
		R = random.randrange(100)
		print("Teclea este numero: "+ str(R))
		time.sleep(1)
		Mensaje = "Tienes solo 1 segundos: "
		Repuesta = input(Mensaje)
		
		if Repuesta == str(R):
			print("Correcto")
			print("Chao")
			time.sleep(2)
			return
		else: 
			print("No carnal")
			print("Espera")
			time.sleep(2)

def daemon():
	logging.debug('Lanzado')
	time.sleep(1)
	logging.debug('Detenido')	




H = threading.Thread(target = PrimerH, args = (1, ))
D = threading.Thread(target = daemon)


H.start()
D.setDaemon(True)
D.start()
#HH.start()