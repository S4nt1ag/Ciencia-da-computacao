import threading
import time

# exemplo de funcao com parametros

def funcao(mensagem):
  for i in range(3):
    print(i, mensagem)
    time.sleep(1)

print('iniciando o programa!')
x = threading.Thread(target=funcao, args=('executando!',))
x.start()
print('finalizando o programa!')