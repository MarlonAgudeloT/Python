SALARIO_MINIMO = 908526

nombre = input("Nombre del trabajador: ")
horas = int(input("Cantidad de horas que se trabajo: "))
valorPorHora = int(input("Valor por hora: "))

valorTotal = 0
valorSaludPension = 0

if horas > 40:
    valorTotal = 40*valorPorHora
    valorTotal = valorTotal + ((horas-40) * (valorPorHora*1.5))
else:
    valorTotal = horas * valorPorHora

if valorTotal >= SALARIO_MINIMO:
   valorSaludPension = valorTotal * 4 / 100
   valorTotal = valorTotal - valorSaludPension 

print("Las ganancias de: ", nombre, "son: ", valorTotal, "sus retenciones en salud y pension",valorSaludPension)

