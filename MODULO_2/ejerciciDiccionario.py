
frutas = {"Platano" : 1.35,"Manzana": 0.80,"Pera": 0.85,"Naranja": 0.70}

while (True):
    frutaIngresadaPorusuario = input("Que fruta desea saber el precio: ")
    numeroDeKilos = input("Cuantos kilos desea comprar: ")
    if frutaIngresadaPorusuario in frutas:
        if numeroDeKilos.isdigit():
            valor = frutas[frutaIngresadaPorusuario]*float(numeroDeKilos)
            print("El valor seria: ",valor)
        else:
            print("No ingreso el numero de kilos")
    else:
        print("Error, no conozco esa fruta")


