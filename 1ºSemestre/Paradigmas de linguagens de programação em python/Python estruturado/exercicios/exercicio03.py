# implementar uma solução em python que resolva a seguinte questão:
# - Calcular o valor de uma compra, sendo que o preço unitário é R$10,00

# - se for feita compra de até 10 unidade não ha descontos
# - Para compras entre 11 e 20 unidades é dado um desconto de 10%
# - acima de 20 unidades, é dado um desconto de 20%

print('mercadão do carlão tudo é 10zão')

quantidade = eval(input('digite quantos produtos está levando: '))
valor = quantidade*10
DEZPORCENT = valor*0.1
VINTEPORCENT = valor*0.2

if (quantidade <= 10):
    print(f'O valor de sua compra é de R${quantidade*10}.00')
elif(quantidade >= 11 and quantidade <= 20):
    desconto = valor - DEZPORCENT
    print(f'O valor de sua compra é de R${desconto}0')
else:
    desconto = valor - VINTEPORCENT
    print(f'O valor de sua compra é de R${desconto}0')