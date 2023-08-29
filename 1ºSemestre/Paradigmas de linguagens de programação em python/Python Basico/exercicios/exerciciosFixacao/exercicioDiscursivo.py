# Como exercício prático, tente escrever um programa para calcular 
# e informar o IMC (índice de massa corpórea) do usuário, que deverá 
# fornecer seu peso e sua altura. Lembre-se de que o IMC é calculado pela fórmula: 

# IMC = Peso/Altura^2

print('calculadora IMC')
peso = eval(input('digite seu peso: '))
altura = eval(input('digite sua altura: '))
IMC = peso/(altura**2)
print(f'O seu imc é: {IMC}')
