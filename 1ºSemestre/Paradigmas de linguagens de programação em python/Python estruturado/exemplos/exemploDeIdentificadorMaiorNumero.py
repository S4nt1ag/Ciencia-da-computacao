# estrategia 1
# a = 10
# b = 20
# if (a>b):
#     maior = a
# else:
#     maior = b
# print(f'O maior numero é: {maior}')

# estrategia 2
# a = 10
# b = 20 
# maior = a
# if(b>maior):
#     maior = b
# print(f'O maior numero é: {maior}')

#minha solução
a = eval(input("digite o primeiro valor: "))
b = eval(input('digite o segundo valor: '))
if(a>b):
    maior = a
else:
    maior = b
print(f'O maior numero entre {a} e {b} é {maior}')