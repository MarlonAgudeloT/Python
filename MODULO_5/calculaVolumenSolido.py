#Calcular el volumen de Una Esfera y Un cono

import math

r1 = 3
h = 9/2
r2 = 4

volumenEsfera = (4 * math.pi *(r1**3))/3

print(volumenEsfera)

volumenCono = ((math.pi*(r2**2)*h))/3

print(volumenCono)

volumenSolido = volumenEsfera + volumenCono

print(volumenSolido)


