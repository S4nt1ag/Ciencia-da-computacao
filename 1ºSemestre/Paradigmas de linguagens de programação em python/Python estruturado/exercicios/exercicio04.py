# Implmentar uma solução em Python que some
# todos os resultados pares de uma lista.

# por exemplo, se alista for [10, 2, 5, 7, 6, 3]
# o resultadp deve ser igual a 18.

lista = [10, 2, 5, 7, 6, 3]
soma = 0
for num in lista:
    if (num%2 == 0):
        soma += num

print(f'o resultado da soma dos pares é: {soma}')