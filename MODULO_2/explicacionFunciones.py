import math

def calcularCuadrado(valor):
    return valor*valor
    print("Hola") #Esto nunca va a salir

def calcularAreaCirculo(radio):
    area = math.pi*radio**2
    return area

def imprimirLista(listado):
    for i in listado:
        print(i)

lista = ["hola","Juan","Pedro"]

imprimirLista(lista)

print(calcularCuadrado(3))

print("El area del circulo con radio 5 es: ",calcularAreaCirculo(5))

def promedio(notas):
    promedio = 0
    for i in notas:
       promedio+=i
    promedio = promedio/len(notas)
    return promedio 

notas = [4,5,4.7]

print("El promedio de las notas es: ", promedio(notas))
