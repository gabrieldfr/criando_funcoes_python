def numero_par():
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        return print('O número digitado é par')
    else:
        return print('O número digitado é ímpar')
print(numero_par())