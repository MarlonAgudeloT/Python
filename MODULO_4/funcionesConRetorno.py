def calcular( importe, descuento):
    print(type(importe),type(descuento))
    return importe - (importe*descuento/100)

datos = [1500,10]

totalCalculo = calcular(*datos)
print(totalCalculo)

