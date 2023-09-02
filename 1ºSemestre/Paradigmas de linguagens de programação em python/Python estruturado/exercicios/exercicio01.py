# implementar uma solução em python que 
#verifique se um Número é par ou impar

print('Verificador sobre par ou ímpar')
a = eval(input('Digite o numero que esteja em duvida: '))

if(a %2 == 0):
    resultado = 'par'
else:
    resultado = 'ímpar'

print(f'O numero {a} é {resultado}')