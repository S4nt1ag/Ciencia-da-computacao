# implementar uma solução que retorne a soma de todos 
# os elementos pares de uma lista

def somaDosPares (lista):
    soma = 0
    for num in lista:
        if(num%2 == 0):
            soma += num
    return soma

teste = [1,2,3,4,5,6,7,8,9]
total = somaDosPares(teste)
print(f'a soma dos numeros pares é: {total}')