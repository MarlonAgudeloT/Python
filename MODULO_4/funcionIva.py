""" Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
y devolver el total de la factura. Si se invoca la función sin 
pasarle el porcentaje de IVA, deberá aplicar un 19%. """


def total_factura(valorNeto,valorIva = 19):
    return valorNeto+valorNeto*valorIva/100


valorACobrar = input("Por favor ingrese el valor de la factura: ")
iva = input("Ingrese el porcentaje de Iva a aplicar: ")
valorTotal = 0

if iva == "":
    valorTotal = total_factura(float(valorACobrar))
else:
    valorTotal = total_factura(float(valorACobrar),float(iva))

print("El valor total de la factura es: ",valorTotal)

