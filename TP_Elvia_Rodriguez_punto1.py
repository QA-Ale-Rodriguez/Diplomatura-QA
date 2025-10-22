#Punto 1 Programa para determinar si un número es primo o no

try:

    numero = int(input("Ingresa un número: "))

    if numero <= 1:
     print("El número no es primo.")
    else:
     es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")

except ValueError:
    print("Debes ingresar un número entero válido.")