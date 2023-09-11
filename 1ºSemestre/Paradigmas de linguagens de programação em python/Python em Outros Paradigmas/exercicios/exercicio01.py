from threading import Thread
from time import sleep

def th1(tempoEspera, mensagem):
  print('\niniciando thread1')
  sleep(tempoEspera)
  print('finalizando thread1')

def th2(tempoEspera, mensagem):
  print('iniciando thread2')
  sleep(tempoEspera)
  print('finalizando thread2')

thread1 = Thread(target=th1, args=(3, 'th1 em ação'))
thread2 = Thread(target=th2, args=(2, 'th2 em ação'))

print('iniciando o executavel')
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('\nencerrando o executavel')