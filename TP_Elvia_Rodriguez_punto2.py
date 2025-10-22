# Variables resultantes de una ecuación cuadrática 

import math

def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"Las raíces son reales y distintas: x1 = {x1}, x2 = {x2}")
    elif discriminante == 0:
        x = -b / (2*a)
        print(f"Las raíces son reales e iguales: x = {x}")
    else:
        print("Las raíces son complejas (no reales).")

try:
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    
    if a == 0:
        print("El valor de 'a' no puede ser 0 en una ecuación cuadrática.")
    else:
        resolver_ecuacion_cuadratica(a, b, c)

except ValueError:
    print("Error: Debe ingresar valores numéricos.")