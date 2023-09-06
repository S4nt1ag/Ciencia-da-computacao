# implementar uma solução que calcule o fatorial de um numero

def calcFatorial(n):
    f = 1 
    for i in range(1, n+1):
        f *= i
    return f

numero = eval(input('digite o numero para calcular o fatorial: '))
resultado = calcFatorial(numero)
print(f'O fatorial de {numero} é: {resultado}')