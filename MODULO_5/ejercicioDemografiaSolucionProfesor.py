"""En 1994 el país A tiene una 
población de 25 millones de habitantes y 
el país B de 19.9 millones. Las tasas de 
crecimiento de la población son de 2% y 3% 
respectivamente.  Desarrollar un algoritmo para 
informar:1. en qué año la población del país B supera 
a la de A 2. En qué año la población del país B duplica 
a la población de A."""

anio = 1994
a = 25.0
b = 19.9
tasaA = 0.02
tasaB = 0.03

aEsMayor = True

def crecimiento (a,b,anio):
    anio +=1
    a = a+(a*tasaA)
    b = b+(b*tasaB)
    print("Poblacion de A", a, "Poblacion de B",b)
    return [a,b,anio] 

while (a>b):
    a,b,anio = crecimiento(a,b,anio)

print("B a superado a A", anio)

while(b<(a*2)):
    a,b,anio = crecimiento (a,b,anio)

print("B es el doble de A en el año", anio)


