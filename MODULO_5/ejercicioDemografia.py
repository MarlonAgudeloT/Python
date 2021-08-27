#Ejercicio crecimiento demografico

"""En 1994 el país A tiene una población de 25 millones de habitantes y el país B de 19.9 millones. 
Las tasas de crecimiento de la población son de 2% y 3% respectivamente.  Desarrollar un algoritmo 
para informar:1. en qué año la población del país B supera a la de A 2. 
En qué año la población del país B duplica a la población de A."""

poblacionPaisA = 25000000

poblacionPaisB = 19900000

tasaCrecimientoA = 2/100

tasaCrecimientoB = 3/100

añoInicio = 1994

contador = 0 

def crecimientoA (poblacionPaisA,tasaCrecimientoA):
        return poblacionPaisA*tasaCrecimientoA

def crecimientoB (poblacionPaisB,tasaCrecimientoB):
        return poblacionPaisB*tasaCrecimientoB
    
incrementoPoblacionA = crecimientoA(poblacionPaisA,tasaCrecimientoA)
incrementoPoblacionB = crecimientoB(poblacionPaisB,tasaCrecimientoB)

while incrementoPoblacionB < incrementoPoblacionA:
    contador += 1
    añoSuperaPoblacion = contador + añoInicio
    
    print("La poblacion del pais B sera mayor a la del pais A en el año: ",añoSuperaPoblacion)
    break








