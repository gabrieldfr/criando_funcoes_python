from math import sqrt
def calcular_raiz_quadrada():
    num = float(input('Digite um número: '))
    raiz_quadrada = sqrt(num)
    return raiz_quadrada
print('A raiz quadrada é: {}'.format(calcular_raiz_quadrada()))