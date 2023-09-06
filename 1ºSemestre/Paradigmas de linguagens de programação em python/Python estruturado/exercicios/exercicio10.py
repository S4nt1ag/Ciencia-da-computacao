# feito por mim

# def verificaNumero():
#   try:
#     numero = int(input('digite um numero: '))
#     print(f'o seu numero é: {numero}')
#   except ValueError:
#     print('Digite apenas numeros, por favor tente novamente')
#     verificaNumero()

# a =  verificaNumero()

# exemplo feito aula

while True:
  try:
    x = int(input('Digite um numero: '))
    break
  except ValueError:
    print('entre com um numero valido')