import threading
import time
def worker():
	print (threading.currentThread().getName(),'Lanzado')
	time.sleep(2)
	print (threading.currentThread().getName(),'Detenido')

def servicio():
	print (threading.currentThread().getName(),'Lanzado')
	print (threading.currentThread().getName(),'Detenido')
t = threading.Thread(target=servicio, name='Hilo 1')
w = threading.Thread(target=worker, name='Hilo 2')
z = threading.Thread(target=worker)
w.start()
z.start()
t.start()