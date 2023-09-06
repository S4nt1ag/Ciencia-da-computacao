# feito por mim

# from tkinter.constants import TRUE
# def divisor():
#   while True:
#     try:
#       numero = int(input('digite por quanto quer dividir: '))
#       if(numero != 0):
#         return numero
#         break
#       else:
#         print('não é possivel dividir por zero, tente outro numero')
#     except ValueError:
#       print('escolha apenas numeros')

# def dividendo():
#   while True:
#     try:
#       numero = int(input('digite o numero que quer dividir: '))
#       return numero
#       break
#     except ValueError:
#       print('digite apenas numeros')

# a = dividendo()
# b = divisor()
# x = a/b

# print(f'{a} dividido por {b} é igual a {x}')

# exemplo

def dividir(x,y):
  try:
    resultado = x / y
    print(f"A resposta é: {resultado}")
  except ZeroDivisionError:
    print('divisão por zero')

dividir(3,0)
dividir(3,2)