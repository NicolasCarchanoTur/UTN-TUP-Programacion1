#FUNCIONES
#Ejercicio 1: Factorial de un número

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

#Ejercicio 2: Serie de Fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

#Ejercicio 3: Potencia recursiva

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

#Ejercicio 4: Conversión de decimal a binario

def decimal_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)

#Ejercicio 5: Palíndromo recursivo

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

#Ejercicio 6: Suma de dígitos

def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

#Ejercicio 7: Pirámide de bloques

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

#Ejercicio 8: Contar dígito en número

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    return contar_digito(numero // 10, digito)



#Bloque principal 

#Ejercicio 1

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    for i in range(1, num + 1):
        print(f"{i}! = {factorial(i)}")

#Ejercicio 2

    num = int(input("Ingrese la posición: "))
    for i in range(num):
        print(fibonacci(i), end=" ")
    print()

#Ejercicio 3

    base = int(input("Base: "))
    exponente = int(input("Exponente: "))
    print(f"{base}^{exponente} = {potencia(base, exponente)}")

#Ejercicio 4

    num = int(input("Ingrese un número decimal: "))
    print(f"Binario: {decimal_a_binario(num)}")

#Ejercicio 5

    palabra = input("Ingrese una palabra: ").lower()
    print("Es palíndromo:", es_palindromo(palabra))

#Ejercicio 6

    num = int(input("Ingrese un número: "))
    print("Suma de dígitos:", suma_digitos(num))

#Ejercicio 7

    n = int(input("Ingrese número de bloques en la base: "))
    print("Total de bloques:", contar_bloques(n))

#Ejercicio 8

    numero = int(input("Ingrese un número: "))
    digito = int(input("Ingrese un dígito (0-9): "))
    print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en {numero}.")
