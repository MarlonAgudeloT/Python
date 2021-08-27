def validarSiTieneHolaMundo():
    if "Hola Mundo" in listaEnteros:
        print("Si lo tiene")
    else:
        print("No lo tiene")


listaEnteros = [1,2,3,4,5]

print(len(listaEnteros))
print(listaEnteros[0])

validarSiTieneHolaMundo()

listaEnteros[2] = "Hola mundo"

validarSiTieneHolaMundo()

if "Hola mundo" in listaEnteros:
    print("Si lo tiene")



