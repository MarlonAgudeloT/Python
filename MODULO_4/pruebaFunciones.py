#Siempre se debe definir primero la función

def saludar(nombre, mensaje="Hola"):
    print(mensaje,nombre)


#saludar("Que mas","Carlos")

saludar(mensaje="Buenos dias", nombre="Claudia")

def nombresEnElCurso(profesor,*estudiantes):
    print("El profesor es: ",profesor)
    print("Los estudiantes son: ")
    for estudiante in estudiantes:
        print(estudiante)

nombresEnElCurso("Luis","Carlos","Daniel", "Pedro")


