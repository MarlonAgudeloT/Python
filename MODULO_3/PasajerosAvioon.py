
asientosPrimera = [None]*5
asientosEconomico = [None]*5

alternativas = 0
alternativasAgotado = 0


while asientosPrimera == [None,None,None,None,None] or asientosEconomico == [None,None,None,None,None]:

    alternativas = int(input("Por favor escriba 1 para Primera clase y Por favor escriba 2 para Economico: "))

    if alternativas == 1:
        asientosPrimera[0]= 1
        print("Pase de abordaje, asiento: ",asientosPrimera[0], "en Primera Clase")
        alternativas = int(input("Por favor escriba 1 para Primera clase y Por favor escriba 2 para Economico: "))
        
    if alternativas == 2:
        asientosEconomico[0]=6
        print("Pase de abordaje, asiento: ",asientosEconomico[0], "en Economico")
        alternativas = int(input("Por favor escriba 1 para Primera clase y Por favor escriba 2 para Economico: "))
    
    if alternativas == 1:
        asientosPrimera [1]= 2
        print("Pase de abordaje, asiento: ",asientosPrimera[1], "en Primera Clase")
        alternativas = int(input("Por favor escriba 1 para Primera clase y Por favor escriba 2 para Economico: "))
    if alternativas == 2:
        asientosEconomico[1]=7
        print("Pase de abordaje, asiento: ",asientosEconomico[1], "en Economico")
        alternativas = int(input("Por favor escriba 1 para Primera clase y Por favor escriba 2 para Economico: "))
    if alternativas == 1:
        asientosPrimera [2]= 3
        print("Pase de abordaje, asiento: ",asientosPrimera[2], "en Primera Clase")
        alternativas = int(input("Por favor escriba 1 para Primera clase y Por favor escriba 2 para Economico: "))
    if alternativas == 2:
        asientosEconomico[2]=8
        print("Pase de abordaje, asiento: ",asientosEconomico[2], "en Economico")
        alternativas = int(input("Por favor escriba 1 para Primera clase y Por favor escriba 2 para Economico: "))
    if alternativas == 1:
        asientosPrimera [3]= 4
        print("Pase de abordaje, asiento: ",asientosPrimera[3], "en Primera Clase")
        alternativas = int(input("Por favor escriba 1 para Primera clase y Por favor escriba 2 para Economico: "))
    if alternativas == 2:
        asientosEconomico[3]=9
        print("Pase de abordaje, asiento: ",asientosEconomico[3], "en Economico")
        alternativas = int(input("Por favor escriba 1 para Primera clase y Por favor escriba 2 para Economico: "))  
    if alternativas == 1:
        asientosPrimera [4]= 5
        print("Pase de abordaje, asiento: ",asientosPrimera[4], "en Primera Clase")
        alternativas = int(input("Por favor escriba 1 para Primera clase y Por favor escriba 2 para Economico: "))
    if alternativas == 2:
        asientosEconomico[4]=10
        print("Pase de abordaje, asiento: ",asientosEconomico[4], "en Economico")
        alternativas = int(input("Por favor escriba 1 para Primera clase y Por favor escriba 2 para Economico: "))

    if asientosPrimera == [1,2,3,4,5]:
        print("No hay mas asientos en Primera clase disponibles")
        alternativasAgotado = int(input("Por favor escriba 1 para Salir o Por favor escriba 2 para elegir un asiento en clase Economico: "))
        if alternativasAgotado == 1:
            print("El proximo vuelo sale en 3 horas")
            exit()

    if asientosEconomico == [6,7,8,9,10]:
        print ("No hay mas asientos en Clase Economica disponibles")
        alternativasAgotado = int(input("Por favor escriba 1 para elegir un asiento en Primera clase o Por favor escriba 2 para salir: "))    
        if alternativasAgotado == 2:
            print("El próximo vuelo sale en 3 horas")
            exit
    if asientosPrimera == [1,2,3,4,5] and asientosEconomico == [6,7,8,9,10]:
        print ("Asientos Agotados")
        exit()      
    else:
        alternativas 

       