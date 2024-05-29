#Ejercicio 3
#Programa modular que calcule la edad dado el año, el año debe leer por el usuario
#a traves del teclado.

def calcularEdad(nac, actual):
    edad= actual - nac
    return edad

print("Ingrese año de nacimiento")
nac = int(input())
print("Ingrese año actual")
actual = int(input())

print("Su edad es"+ str(calcularEdad(nac,actual)))

# Próximamente más ejercicios 
