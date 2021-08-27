import json

import requests

with open("JsonEjercicio2File.json", "r",encoding ="utf-8") as archivo_entrada:
    usuarios = json.load(archivo_entrada)
print(usuarios)


dict_nuevo = dict()

for llave in usuarios:
    diccionario_usuario = usuarios[llave]
    for deporte in diccionario_usuario["deportes"]:
        if not deporte in dict_nuevo.keys():
            dict_nuevo[deporte]=[llave]
        else:
            dict_nuevo[deporte].append(llave)

print(dict_nuevo)

with open("deportes_filtrado.json", "w") as archivo_salida:
    json.dump(dict_nuevo , archivo_salida, ensure_ascii=False)