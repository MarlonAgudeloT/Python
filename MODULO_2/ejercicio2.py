""" Buscar el número 23 en la siguiente lista:
a=[11,34,12,55,3,56,3,32,56,43,77,23,45,67,23,67]
y saber que tanto tuvo que recorrer hacia adelante y hacia atrás, para ello utilice el método reverse"""


# Sin inverso
a=[11,34,12,55,3,56,3,32,56,43,77,23,45,67,23,67]

contador = 0

for valor in a:
    contador +=1
    if valor == 23:
        print("Lo encontre!", contador)

# Con reversed
print("Usando for reversed")
contador = 0

for valor in reversed(a):
    contador +=1
    if valor == 23:
        print("Lo encontre!", contador)

        






