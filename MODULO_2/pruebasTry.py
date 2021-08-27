def division(a, b):
    try:
        coc = a // b
        res = a % b
        return(coc, res)
    except:
        print("Error en la division de", a, "entre", b)
        return ""

print(division(10, 0))
print(division(1024, 10))

c = 1024%10
print(c)


