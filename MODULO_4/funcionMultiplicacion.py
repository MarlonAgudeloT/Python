def sumar(numero1,numero2):
    return numero1+numero2

def multiplicar (numUno,numDos):
    valor = 0
    for i in range(0,numDos):
        valor = sumar(valor,numUno)
    return valor 

print(multiplicar(2,4))



