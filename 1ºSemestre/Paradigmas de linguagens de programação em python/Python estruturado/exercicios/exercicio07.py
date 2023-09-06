def numeroPrimo(num):
    if(num<2):
        return False
    i = num // 2
    while (i > 1):
        if(num%i == 0):
            return False
        i -= 1
    return True

def mensagemFinal (numero, resultado):
    if(resultado == False):
        return f"O numero {numero} não é primo"
    else:
        return f"O numero {numero} é primo"
    
numero = eval(input('digite o numero que deseja saber se é primo ou não: '))
resultado = numeroPrimo(numero)
msg = mensagemFinal(numero, resultado)
print(msg)