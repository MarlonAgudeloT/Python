try:
  var1 = int(input("Ingrese el primer valor: "))
  var2 = int(input("Ingrese el segundo valor: "))
  total = var1+var2
except ValueError:
  print("Los tipos de datos no cuadran para hacer la operación")
except Exception as e:
  print(e,"\n",type(e))
print(total)