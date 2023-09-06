# Sabemos que é possível importar módulos e chamar funções desses módulos em Python.
# Considere o módulo math, que oferece diversas funções matemáticas. Uma dessas funções
# é a ceil(x), que retorna o menor inteiro maior ou igual a x. Suponha que um estudante
# queira usar uma variável n, que recebe o valor 5.9, e, em seguida, imprimir na tela o
# menor inteiro maior ou igual a ela. O código correto é:


import math
n = 5.9
print(math.ceil(n))