import os

print("Bienvenido al sistema de ubicación para zonas públicas WIFI") #Mensaje de bienvenida

NOMBRE_DE_USUARIO = "51716" #El nombre de usuario es el codigo del grupo al que pertenezco de fundamentos de programación
CONTRASEÑA = "61715" #La contraseña es el codigo del grupo ade forma inversa.
DIGITOS = 716 # Son los ultimos 3 digitos del codigo del grupo
OPERACION_OCULTA = round((((6%6)*1/6)+7)%5-1) #Esta operacion debe dar como resultado el penultimo numero del codigo = 1
usuario=0
password=0
captcha=0

usuario = input("Ingrese el nombre de usuario: ") #Debe ingresar el codigo del grupo al que estoy asignado = 51716

if usuario == NOMBRE_DE_USUARIO:  #Esta condicion se debe cumplir para pedir la contraseña
    password = input("Por favor ingrese la contraseña: ")
    if password == CONTRASEÑA: # Debe ser igual a la contraseña asignada para posteriormente pedir el Captcha
        captcha = int(input("Debe resolver la siguiente suma para validar que es un humano: " + str(DIGITOS) +  "+"  +  str(OPERACION_OCULTA) +  "="  )) #Debe resolver la suma para continuar
        if captcha == DIGITOS + OPERACION_OCULTA: # Con esta condicion se valida que el usuario resolvio la operación 
            print("Sesión iniciada")
            
            #Ponemos todas las opciones de menu posibles
            OpcDeMenu = [". Cambiar contraseña",". Ingresar coordenadas actuales",". Ubicar zona wifi más cercana", 
            ". Guardar archivo con ubicación cercana", ". Actualizar registros de zonas wifi desde archivo ",
            ". Elegir opción de menú favorita",". Cerrar sesión"]
            
            def menu(opcion = 0, favorito = 0, contador = 0):
                if opcion == 0 and favorito == 0:
                    for i in range(0,len(OpcDeMenu)):
                        print(str(i+1) + OpcDeMenu[i])    
            
                #Validando los errores
                if contador == 2:
                    print("Error")
                    exit()
                
                #En este paso el usuario debe elegir la opcion de desea
                if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
                    print("Usted ha elegido la opción",opcion)
                    exit() #Usamos el comando exit() para salir del programa
                
                #Si escoge la opcion de menu favorito 1
                if favorito == 1:
                    for i in range(0,len(OpcDeMenu)):
                        print(str(i+1)+OpcDeMenu[i])

                #Si escoge la opcion de menu favorito 2
                if favorito == 2:
                    OpcDeMenuNuevo = [". Ingresar coordenadas actuales",". Cambiar contraseña",
                    ". Ubicar zona wifi más cercana",". Guardar archivo con ubicación cercana",". Actualizar registros de zonas wifi desde archivo ",
                    ". Elegir opción de menú favorita",". Cerrar sesión"]
                    for i in range(0,len(OpcDeMenuNuevo)):
                        print(str(i+1)+OpcDeMenuNuevo[i])
                
                #Si escoge la opcion de menu favorito 3
                if favorito == 3:
                    OpcDeMenuNuevo = [". Ubicar zona wifi más cercana",". Cambiar contraseña",". Ingresar coordenadas actuales",
                    ". Guardar archivo con ubicación cercana", ". Actualizar registros de zonas wifi desde archivo ",
                    ". Elegir opción de menú favorita",". Cerrar sesión"]
                    for i in range(0,len(OpcDeMenuNuevo)):
                        print(str(i+1)+OpcDeMenuNuevo[i])

                #Si escoge la opcion de menu favorito 4
                if favorito == 4:
                    OpcDeMenuNuevo = [". Guardar archivo con ubicación cercana",". Cambiar contraseña",". Ingresar coordenadas actuales",". Ubicar zona wifi más cercana", 
                    ". Actualizar registros de zonas wifi desde archivo ",". Elegir opción de menú favorita",". Cerrar sesión"]
                    for i in range(0,len(OpcDeMenuNuevo)):
                        print(str(i+1)+OpcDeMenuNuevo[i])
                
                #Si escoge la opcion de menu favorito 5
                if favorito == 5:
                    OpcDeMenuNuevo = [ ". Actualizar registros de zonas wifi desde archivo ",". Cambiar contraseña",". Ingresar coordenadas actuales",". Ubicar zona wifi más cercana", 
                    ". Guardar archivo con ubicación cercana",". Elegir opción de menú favorita",". Cerrar sesión"]
                    for i in range(0,len(OpcDeMenuNuevo)):
                        print(str(i+1)+OpcDeMenuNuevo[i])
                    
                #En este paso el usuario debe validar la eleccion de la opcion favorita
                if opcion == 6:
                    contador = 0
                    favorito = int(input("Seleccione opción favorita"))
                    if favorito < 1 or favorito > 5:
                        print("Error")
                        exit()
                    else:
                        #Adivinanza 1 para confirmar la decisión
                        respuestaUno = int(input("Para confirmar por favor responda: Cuando te pones a contar por mi tienes que empezar"))
                        if respuestaUno != 1:
                            print("Error")
                            menu()
                        else:
                            #Adivinanza 2 para confirmar la decisión
                            respuestaDos = input("Para confirmar por favor responda: Si le sumas su hermano gemelo al numero tres ya sabes cual numero es")
                            if respuestaDos != "6":
                                print("Error")
                                menu()
                            else:
                                #Con este else limpiamos la terminal
                                os.system ("cls")
                                menu(0,favorito)

                #Si elige la opcion 7 se cierra el programa y se despide con un "Hasta pronto"
                if opcion == 7:
                    print("Hasta pronto")
                    exit()
                
                # Este if lo usamos para contar el numero de errores que puede cometer el usuario hasta que el programa sea cerrado
                if opcion < 1 or opcion > 7:
                    if opcion != 0:
                        print("Error")
                        contador+=1
                
                #Se solicita ingresar nuevamente la opcion de menu
                opcion = int(input("Elija una opción"))
                menu(opcion, 0 , contador)
            
            menu()

        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")




