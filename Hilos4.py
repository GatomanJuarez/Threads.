import threading 
import logging
import time

logging.basicConfig(level=logging.DEBUG, 
format='[%(levelname)s] - %(threadName)-10s : %(message)s')

def daemon():
	logging.debug('Lanzado')
	time.sleep(2)
	logging.debug('Detenido')

def hilo():
	print("texto")
	time.sleep(4)

d = threading.Thread(target=daemon, name='Daemon')
e = threading.Thread(target=hilo, name='Hilo')
d.setDaemon(Truen)
d.start()
e.start()
print(e.isAlive());