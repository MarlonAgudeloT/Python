#Explicacion for 3

notasDelCurso = [3.5, 4.5, 4.2, 2.8, 3.0]
contador = 0
promedio = 0

for nota in notasDelCurso:
    promedio = promedio + nota
    contador = contador + 1
promedio = promedio / contador

print("Promedio Total", promedio)