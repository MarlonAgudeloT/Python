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
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")







