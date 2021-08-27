#Desarrollar un algoritmo que imprima de manera 
# ascendente los valores todos del mismo
# tipo de un diccionario

import operator

puertos = {22:"SSH",23:"telnet",80:"Http"}

puertos_sort = sorted(puertos.items(),key = puertos.itemgetter(1), reverse=False)

print(puertos_sort)

