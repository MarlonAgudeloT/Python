"""print("Por favor ingrese las notas que saco en cada asignatura")
diccionario = dict()

diccionario["Matematicas"] = input("Ingreses la nota que saco en Matematicas: ")
diccionario["Fisica"] = input("Ingreses la nota que saco en Fisica: ")
diccionario["Qumica"] = input("Ingreses la nota que saco en Quimica: ")
diccionario["Historia"] = input("Ingreses la nota que saco en Historia: ")
diccionario["Lenguaje"] = input("Ingreses la nota que saco en Lenguaje: ")

print(diccionario)

"""
lista = (["Matematicas"],["Fisica"],["Qumica"],["Historia"],["Lenguaje"])

for materia in lista:
    materia.append(input("Que nota saco en "+materia[0]+": "))

for materia in lista:
    print("En "+materia[0]+" has sacado: " + materia[1])

