#Calcular el interes compuesto de un credito pagado en n periodos

def interesCompuesto(p,i,n):
    return p *(1+i)**n


p = 1000000

i = 0.03

n = 2

cantidadAPagar = interesCompuesto(p,i,n) 

print("El valor a pagar es: $", cantidadAPagar)