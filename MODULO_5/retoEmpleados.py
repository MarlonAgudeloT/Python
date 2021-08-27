#Reto Empleados Unal

#Igresar el nombre 

"""
nombreTrabajador = " "

nombreTrabajador = input("Por favor ingrese su nombre: ")

valorBruto = int(input("Por favor ingrese el valor bruto devengado"))

tipoDeContrato = input("Por favor especifique su tipo de contrato, contratista o de planta: ")


if tipoDeContrato is True:
    tipoDeContrato == "contratista"
        tipoHonorarios = input("Su contrato es por Honorarios o Servicios?")
        if tipoHonorarios is True:
            tipoHonorarios == "Honorarios"
            print("Usted es contratista por honorarios")
    

"""
#Solucion profesor
SALARIO_MINIMO_LEGAL_VIGENTE = 908526
def calcularparafiscalesEmpresa(contratista,salario):
    sena=0
    ICBF = 0
    ccf = 0
    salud = 0
    pension = 0
    subsidioTransporte = 0.0
    if contratista == 2:
        sena = salario * 2/100
        ICBF = salario * 3/100
        ccf = salario * 4/100
        salud = salario * 8.5/100
        pension = salario * 12/100
        if salario <= SALARIO_MINIMO_LEGAL_VIGENTE*2:
            subsidioTransporte = 106453.0
    return [sena,ICBF,ccf,salud,pension,subsidioTransporte]

def calcularparafiscalesEmpleado (contratista, salario):
    salud = 0
    pension = 0
    if contratista == 1:
        baseGravable = salario * 40/100
        if (baseGravable <SALARIO_MINIMO_LEGAL_VIGENTE):
            baseGravable = SALARIO_MINIMO_LEGAL_VIGENTE
        salud = baseGravable * 12.5 /100
        pension = baseGravable * 16/100
    else:
        salud = salario * 4/100
        pension = salario * 4/100
    return [salud,pension]

def calcularretencionFuente(declarante,honoriarios,salario):
    retencion = 0
    if declarante:
        if honorarios:
            retencion = salario * 11/100
        else:
            retencion = salario * 4/100
    
    else:
        if honorarios:
            retencion = salario *10/100
        else:
            retencion = salario *6/100




parafiscalesEmpresa = [0,0,0,0,0,0]
parafiscalesEmpleado = [0,0]
retencionDeFuente = 0

nombreTrabajador = ""
salario = 0.0
contratista = 0
valorTotalARetener = 0.0
total = 0.0

arregloTotal = ()

while True:
    for trabajador in arregloTotal:
        print(trabajador)
        nombreTrabajador = input("Ingrese el nombre del trabajador: ")
        salario = float(input("Salario a devengar del trabajador: "))
        contratista = int(input("Ingrese 1 para contratista, 2 para personal de planta: "))
        if contratista == 1:
            declarante = input("A. Declarante de Renta, B. No declarante de renta")
            honorarios = input("1. Honorarios, 2. Servicios")
            if declarante == "A":
                declarante = True
            else:
                declarante = False

            if honorarios == "1":
                honorarios = True
            else:
                honorarios = False
                retencionDeFuente = calcularretencionFuente(declarante,honorarios,salario)
        else:
            retencion = 0

        parafiscalesEmpresa = calcularparafiscalesEmpresa(contratista,salario)
        parafiscalesEmpleado = calcularparafiscalesEmpleado(contratista,salario)
        retencionDeFuente = calcularretencionFuente(declarante,honorarios,salario)

        dataTrabajador = {"nombre":nombreTrabajador,"salario":salario,"parafiscalesEmpresa": parafiscalesEmpresa, "parafiscalesEmpleado":parafiscalesEmpleado}
        arregloTotal.append(dataTrabajador)
        print("El trabajador: ",nombreTrabajador,", con salario de: ", salario,", a la empresa le corresponde: ",  )