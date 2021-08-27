"""Escriba una aplicación que muestre los siguientes patrones por separado, uno debajo del otro. 
Use ciclos for para generar los patrones. Todos los asteriscos (*) deben imprimirse 
mediante una sola instrucción print. No debe haber ninguna otra instrucción de salida en el programa.
 [Sugerencia: los últimos dos patrones requieren que cada línea empiece con un número apropiado 
 de espacios en blanco]."""
"""
a = "*"
iteraciones =0
contador = 0
for esquema in a:
    iteraciones <=10
    contador +=1
    print(a*contador ,"\n")
"""
a = "*"
espacio = " "

for i in range(0,10):
    print(a*i)

print("")
for i in reversed(range(0,10)):
    print(a*i)

print("c.")
for i in range(0,10):
    print(espacio*(i) + (a*(10-i)))

print("d.")
for i in range(0,10):
    print((espacio*(i) + (i*10))


