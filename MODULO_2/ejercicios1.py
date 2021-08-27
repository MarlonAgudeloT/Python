# 1 Crear un programa que imprima los numeros del 1 al 100
# pero omitiendo los que son divisibles por 11 y que el programa nos diga
# cuantos son los numeros divisibles por 11

contador = 0

for valorEnCajita in range(1,101):
    if valorEnCajita%11 == 0:
        contador+=1
        continue
    print(valorEnCajita)
print("Los dividenodos de 11 son", contador)

        