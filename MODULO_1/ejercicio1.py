#Lanzamiento de Sam
print("Lanzamiento de Sam")
lanzamientoSam = int(input("Cuantos metros lanzo Sam?: "))

lanzamientoBucky = 4 + lanzamientoSam + lanzamientoSam

lanzamientoJhonW = lanzamientoSam+lanzamientoBucky

lanzamientoJhonW = lanzamientoJhonW/5

categoria = ""
print("En que categoria quedo el lanzamiento de Jhon Walker?")
if lanzamientoJhonW >= 0 and lanzamientoJhonW <=20:
    categoria = "Quedo en la Categoria 1"
else:    
    if lanzamientoJhonW >=21 and lanzamientoJhonW <=30:
        categoria = "Quedo en la Categoria 2"
    else:
        if lanzamientoJhonW >=31 and lanzamientoJhonW <=50:
            categoria = "Quedo en la Categoria 3"
        else:
            if lanzamientoJhonW >50:
                categoria = "Quedo en la Categoria 4"

print(lanzamientoSam, lanzamientoBucky, lanzamientoJhonW)
print(categoria)


           


