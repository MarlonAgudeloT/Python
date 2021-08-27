"""Desarrollar un programa que dada una listas de personas, cada persona representada como el siguiente ejemplo:
{"nombres":"Pedro Julio", "apellidos":"Tristán Merchán",
"edad":101}, imprima los nombres y apellidos de las personas que están en un rango de edades."""
"""
lista_personas= [["Nombres","Pedro Julio"],["Apellidos","Tristan Merchan"]]


x = 4
x *= 3 

#print(x)

#print(name:=input())

#print(False or True)   """
"""
nums = [1,2,3,4]

nums.insert(1,6)

print(nums)"""

"""i = 3
while i>=0:
   print(i)
   i = i - 1"""

def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            # (Fill in the missing line here)
            return max_num
    print(max_num)