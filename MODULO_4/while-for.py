USUARIO_CORRECTO = "andres.salamanca"
CONTRASENIA_CORRECTA = ""

usuario = ""
contrasenia = ""
CantidadIntentos = 3
UsuarioIngresado = True

while UsuarioIngresado:
    if usuario != USUARIO_CORRECTO: 
        usuario = input("Ingrese su usuario: ")
    contrasenia = input("Ingrese su contraseña: ") # Aqui es donde se diferencia para que no vuelva a pedir el usuario si es correcto

    if usuario == "andres.salamanca" and contrasenia == "123":
        print("Bienvenido")
        UsuarioIngresado = False
    else:
        #Cantidad de intentos = Cantidad de Intentos +1
        CantidadIntentos -= 1
        print("Usuario o contraseña erronea, le permitimos", CantidadIntentos, "antes de blquear el usuario")
        if CantidadIntentos == 0:
            print("Se bloquea el usuario")
            break
