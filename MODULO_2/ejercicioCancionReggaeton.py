import random
"""
listaUno = ["Mami","Yo Quiero","Encenderte","Suave","Hasta Que Salga El Sol","Sin Anestesia"]
listaDos = ["Bebe","Yo Puedo","Amarte","Lento","Toda La Noche","Sin Compromiso"]
listaTres = ["Princess","Yo Vengo A","Ligar","Rapido","Hasta El Amananecer","Feis to Feis"]
listaCuatro = ["Mami","Voy A","Jugar","Fuerte","Todo El Dia","Sin Miedo"]
def ram(a):
    a = random.randint(0,3)
    return a
print(listaUno[ram(0)],listaDos[ram(0)],listaTres[ram(0)],listaCuatro[ram(0)])
"""

#Solucion del Profesor
def seleccionarPalabra(tupla):
    numeroAleatorio = random.randint(0,3)
    return tupla[numeroAleatorio]

tuplaUno = ("Mami","Bebe","Princess","Mami")
tuplaDos = ("Yo Quiero","Yo Puedo","Yo Vengo A","Voy A")
tuplaTres = ("Encenderte","Amarte","Ligar","Jugar")
tuplaCuatro = ("Suave","Lento","Rapido","Fuerte")
tuplaCinco = ("Hasta Que Salga El Sol","Toda La Noche","Hasta El Amananecer","Todo El Dia")
tuplaSeis = ("Sin Anestesia","Sin Compromiso","Feis to Feis","Sin Miedo")

frase = ""
frase = seleccionarPalabra(tuplaUno)+ " " + seleccionarPalabra(tuplaDos)+ " " + seleccionarPalabra(tuplaTres) + " " + seleccionarPalabra(tuplaCuatro) + " " + seleccionarPalabra(tuplaCinco) + " " + seleccionarPalabra(tuplaSeis)

frase = frase.replace("r","l")
print(frase)
