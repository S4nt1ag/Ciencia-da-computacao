from threading import Thread
from time import sleep

def th1(tempoEspera, mensagem):
  print(f'\ncalculando o cubo de: {mensagem} da th1')
  sleep(tempoEspera)
  print('o cubo da th1 ',mensagem**3)

def th2(tempoEspera, mensagem):
  print(f'calculando o quadrado de: {mensagem} da th2')
  sleep(tempoEspera)
  print('o quadrado da th2 ',mensagem**2)

thread1 = Thread(target=th1, args=(3, 5))
thread2 = Thread(target=th2, args=(2, 10))

print('iniciando o executavel')
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('\nencerrando o executavel')