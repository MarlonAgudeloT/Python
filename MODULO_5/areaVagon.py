import math

a = 5

b = 10

r = 3


def areaRectangulo (a,b):
    return a * b

def areaCirculo (r):
    return (math.pi * r**2)

print(areaRectangulo(a,b)+areaCirculo(r)+areaCirculo(r))





