#Ejercicio 1
#Crear un programa modular que calcule el area de un triangulo valores de entrada por teclado
def calcularArea(a, b):
    area = (b* a)/2
    return area

print("Ingresar altura") 
a= float(input())
print("Ingresar base")
b= float(input())

print("El area es"+ str(calcularArea(a, b)))




 




