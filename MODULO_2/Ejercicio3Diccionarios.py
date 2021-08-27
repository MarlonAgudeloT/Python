
diccionario1 = {"Ana":1000,"Alvaro":3000,"Genaro": 1600}
diccionario2 = {"Luis":3000,"Alirio":4500,"Ana":3500}

resultado = diccionario2.copy()
resultado.update(diccionario1)
print(resultado)
"""

def mezcla_diccionarios (diccionario1,diccionario2):
    diccionarioNuevo = diccionario1.update(diccionario2)
    
    return diccionarioNuevo

print(mezcla_diccionarios,diccionario1,diccionario2)"""