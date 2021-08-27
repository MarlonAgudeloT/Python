#Calcule el valor de π a partir de la serie infinita: 
 
#Imprima una tabla que muestre el valor aproximado de π, 
#calculando un término de esta serie, dos términos, tres, etcétera. 
# ¿Cuántos términos de esta serie tiene que utilizar para obtener 3.14? ¿3.141? ¿3.1415? ¿3.14159?
"""
n=2
i=3
contador = 0
pi = 4-((4/i)+(4/i+n)-(4/i+n))

while pi <= 3.14159:
    contador +=1
    print(pi) """

pi= 0
contador = 1
iteracione = 1
a = [3.14, 3.141, 3.1415, 3.14159]

iteracionDelFor = 2
for versionPi in a:
    contador = 1
    iteraciones = 1
    while True:
        if iteraciones%2==1:
            pi +=4/contador
        else:
            pi -= 4/contador
        if round(pi,iteracionDelFor) == versionPi:
            print("Pi: ", pi, "Aproximacion", round(pi,iteracionDelFor))
            break
        contador +=2
        iteraciones +=1
    iteracionDelFor+=1


    

