# implemente uma solução que calcule equações de segundo grau
# exemplo: dada a equação x² + 5x + 6 = 0, as raizes são {-3 e -2}

#meu codigo abaixo

# def calculoDelta(a, b, c):
#     DELTA = (b*b) - 4*a*c
#     if(DELTA < 0):
#         return False
#     else:
#         return DELTA

# def calculoSegundoGrau(a, b, c):
#     delta = calculoDelta(a, b, c)
#     SEGUNDOGRAU1 = (-(b) + delta**(1/2))/ 2*a
#     SEGUNDOGRAU2 = (-(b) - delta**(1/2))/ 2*a
#     total = [SEGUNDOGRAU2, SEGUNDOGRAU1]
#     totalAlt = [SEGUNDOGRAU2]
#     if( delta == False):
#         return False
#     elif( delta == 0):
#         return totalAlt
#     else:
#         return total


# def mensagemFinal(resultado):
#     if (resultado == False):
#         return 'a equação não possui raizes com numeros reais'
#     else:
#         return resultado


# equacao = calculoSegundoGrau(1,5,6)
# resultado = mensagemFinal(equacao)

# print(resultado)


# codigo do exemplo 

def entradaDeDados():
    coeficiente = quantidade = eval(input('digite o valor do coeficiente: '))
    return coeficiente

def calcDelta(a,b,c):
    delta = b*b-4*a*c
    return delta

import numpy as np 
def calcularRaizes(a,b,c,delta):
    if (delta < 0):
        resultado = 'a equação não possui raizes com numeros reais'
    elif(delta==0):
        x=-b/(2*a)
        resultado=f'a equação possui apenas a raiz: {x}'
    else:
        x1=(-b-np.sqrt(delta))/(2*a)
        x2=(-b+np.sqrt(delta))/(2*a)
        resultado = f'a equação possui as raizes: {x1} {x2}'
    return resultado


a = entradaDeDados()
b = entradaDeDados()
c = entradaDeDados()

delta = calcDelta(a,b,c)

resultado = calcularRaizes(a,b,c,delta)
print(resultado)