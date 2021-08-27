mayor = 0

print("Antes",mayor)

for valor in [3,41,12,9,74,15]:
    if valor > mayor:
        mayor = valor
    print("Bucle", mayor)
print("Despues", mayor)
