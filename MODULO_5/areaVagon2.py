import math

def areaRectanguloMayor (a1,b1):
    return a1*b1

def areaRectanguloMenor (a2,b2):
    return a2*b2

def areaCirculoMenor (r1):
    return math.pi * r1**2

def areaCirculoMayor (r2):
    return math.pi * r2**2

a1 = 5

b1 = 10

a2 = 3

b2 = 6

r1 = 4

r2 = 2

AreaTotal = areaRectanguloMayor(a1,b1)+areaRectanguloMenor(a2,b2)+areaCirculoMayor(r1)+areaCirculoMenor(r2)

print(AreaTotal)

