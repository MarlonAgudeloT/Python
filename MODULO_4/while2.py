# Si el numeor es divisor de 7
contador = 0

while contador <= 2000:
    contador +=1
    if contador % 7 == 0:
        print(contador)    
    #else:
        #print("El numero",contador,"no es divisible por 7")
        #contador += 1
        #continue (ignora todo lo que se ponga de aqui para abajo)