import threading
import time

# exemplo de funcao sem parametros

def funcao():
  for i in range(3):
    print(i, ' executando a thread!')
    time.sleep(1)

print('iniciando o programa!')
threading.Thread(target=funcao).start()
print('finalizando o programa!')