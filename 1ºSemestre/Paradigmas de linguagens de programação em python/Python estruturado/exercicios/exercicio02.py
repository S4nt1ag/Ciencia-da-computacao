# Implementar uma solução que resolva a seguinte questão:
# - se nota for maior ou igual a 7, o estudante foi aprovado.
# - se aa nota for menor que 7 e maior ou igual a 5, o estudante
# esta em recuperação
# - se a nota for menor que 5, o estudante está reprovado.

print('Escola Estadual o mundo ensina')
nota = eval(input('para saber sua situação digite sua nota: '))

if(nota >= 7):
    print('Parabéns você foi APROVADO')
elif(nota < 7 and nota >= 5):
    print('Você está de RECUPERAÇÃO')
else:
    print('Você foi REPROVADO')