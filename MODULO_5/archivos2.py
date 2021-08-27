informacion = ""
with open ("files/Marlondata.txt","a+") as f:
    informacion = f.read(6) # Asi me muestra 
print(informacion)