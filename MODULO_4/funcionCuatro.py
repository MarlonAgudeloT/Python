def funcion():
    return "Hola mundo"

def llamadaDeRetorno (func=""):
    if func in globals():
        return globals([func]("Laura"))
    else:
        return "Funcion no encontrada"

nomDeLaFuncion = "funcion"
prin(locals()[nombreDeLaFuncion]())
