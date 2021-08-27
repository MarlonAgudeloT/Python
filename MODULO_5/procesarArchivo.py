
with open("files/SalesJan2009.csv", "r", encoding="utf-8") as f:
    lista = f.read()

medio_de_pago = input("Introduzca el medio de pago a buscar: ")

print("Medio de pago", medio_de_pago , "y el numero de pagos es: ", lista.count(medio_de_pago))
        

