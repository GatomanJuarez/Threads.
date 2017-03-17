import threading
def worker():
	print ('Estoy trabajando')
threads = list()
for i in range(3):
	t = threading.Thread(target=worker)
	threads.append(t) """Agrega el hilo a threads"""
	t.start()
	