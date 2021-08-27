# Explicacion for 2
base = int(input("Ingrese la base: "))
potencia = int(input("Ingrese el exponencial: "))
total = 1

for exponente in range(1,potencia):
    total = total * base
    print(exponente)

print("Total: ",total)


