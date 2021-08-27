diccionario = dict()
print(diccionario)

diccionario["Hola"] = "Hello"
diccionario["Bienvenido"] = "Wellcome"
diccionario["Adios"] = "Bye"

print(diccionario)

#Para ordendar un listado
listadoOrdenado = list(diccionario.keys())
print(listadoOrdenado)
listadoOrdenado.sort()

print(diccionario["Bienvenido"])

print(diccionario["Adios"])

print("Hola" in diccionario)


