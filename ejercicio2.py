import math
#Ejercicio 2
#Crear un programa que calcule el area de un circulo
def calcularAreaCirculo(r):
    area= math.pi *pow(r, 2)
    return area
print("Ingrese radio del circulo")
r= float(input())

print("El area del circulo es " + str(calcularAreaCirculo(r)))



