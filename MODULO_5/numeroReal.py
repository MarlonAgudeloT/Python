"""Dado un nu ́mero real x, construya una funci ́on que permita determinar si el nu ́mero es positivo, 
negativo o cero. Para cada caso de debe imprimir el texto que se especifica a continuaci ́on:
Positivo: “El n ́umero x es positivo”
Negativo: “El n ́umero x es negativo”
Cero (0): “El n ́umero x es el neutro para la suma”"""

x = int(input("Por favor ingrese un numero real: "))

def numeroReal (x):
    if x > 0:
        print("El numero",  x , "es positivo")
    if x < 0:
        print("El numero" , x ,  "es negativo")
    if x==0:
        print("El numero" , x ,  "es neutro para la suma")

numeroReal(x)





