import json

import requests

with open("JsonEjercicio2File.json", "r",encoding ="utf-8") as archivo_entrada:
    usuarios = json.load(archivo_entrada)
print(usuarios)

deporte = input("Ingrese el deporte a buscar: ")
listaDeDeportistas = list()

for usuario in usuarios:
    diccionarioPorUsuario = usuarios[usuario]
    if deporte in diccionarioPorUsuario["deportes"]:
        listaDeDeportistas.append(diccionarioPorUsuario["nombres"]+" "+diccionarioPorUsuario["apellidos"])

print(listaDeDeportistas)

rango_baja = int(input("Ingrese edad desde: "))
rango_alta = int(input("Ingrese edad hasta"))
listaPorEdades = list()

for usuario in usuarios:
    diccionarioPorUsuario = usuarios [usuario]
    if rango_baja <= rango_alta and rango_alta >= rango_baja:
        listaPorEdades.append(diccionarioPorUsuario["nombres"]+" "+diccionarioPorUsuario["apellidos"])

print("Esta es la lista por Edades: ",listaPorEdades)
