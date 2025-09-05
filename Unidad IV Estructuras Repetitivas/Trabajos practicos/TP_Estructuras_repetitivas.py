"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""

#Bucle for desde 0 hasta 101 ya que range excluye el extremo superior
for i in range(0, 101, 1): 
    print(i) #Imprimir i

"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""

numero_entero = input("Ingrese un numero entero: ")

#Verificacion para saber si el dato ingresado son solo digitos enteros positivos o negativos
if numero_entero.lstrip("-").isdigit():
    numero = int(numero_entero)
    print("Numero valido: ", numero)
else:
    print("No ingreso un numero valido")

numero = abs(numero) #Quita el signo "-" 

if numero == 0:
    cantidad_digitos = 1
else:
    cantidad_digitos = 0
    while numero > 0: #Se divide el numero ingresado entre 10 contanto los pasos y eso dara como resultado la cantidad de digitos
        numero //= 10
        cantidad_digitos += 1

print(cantidad_digitos)

"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

num_uno = int(input("Ingrese el primer numero: "))
num_dos = int(input("Ingrese el segundo numero: "))

num_uno = num_uno + 1
suma = 0

for i in range(num_uno, num_dos):
    suma += i 

print(f"La suma de los números entre {num_uno} y {num_dos}, excluyéndolos, es: {suma}")

"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

#Inicializo variables
num = None
suma = 0 

#Mientras el numero ingresado sea diferente a 0 se sumaran los numeros
while num != 0:
    num = int(input("Ingrese un numero: "))
    suma = num + suma

#Imprimo por pantalla el resultado de la suma 
print(suma)

"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""
import random 

#Inicializo variables
num = None
num_aleatorio = random.randint(0, 9)
intentos = 0

#Bucle while que se ejecutara hasta que el numero ingresado sea igual al numero aleatorio
while num != num_aleatorio:
    num = int(input("Ingrese un numero: "))
    intentos += 1 #Se suman los intentos

#Imprimo cual es el numero aleatorio y la cantidad de intentos 
print(f"Correcto! El numero es {num_aleatorio}. Lo hiciste en {intentos} intentos")

"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""

#Se imprimen numeros pares en forma decreciente de 100 a 0 (Incluyendo el 0 al poner -1)
for num in range(100, -1, -2):
    print(num)

"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""

num_entero = int(input("Ingrese un numero: "))
suma = 0 

for num in range(0, num_entero + 1, 1 ):
    suma = suma + num
    
print(suma)

"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

numero_par = 0
numero_impar = 0
numero_negativo = 0
numero_positivo = 0

for i in range(5):
    num = int(input("Ingrese un numero: "))

    if num % 2 == 0:
        numero_par += 1
    else:
        numero_impar += 1
    
    if num > 0:
        numero_positivo += 1
    elif num < 0:
        numero_negativo += 1

print()
print(f"Numeros positivos: {numero_positivo}")
print(f"Numeros negativos: {numero_negativo}")
print(f"Numeros par: {numero_par}")
print(f"Numeros impar: {numero_impar}")

"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""

#Defino variables
numeros = 100
suma = 0
i = 0

#Bucle for para ingresar la cantidad de numeros definida 
for i in range(numeros):
    num = int(input(f"Ingrese el numero {i+1} : "))
    #Suma de los numeros que van ingresando
    suma += num

#Calculo para sacar la media entre los numeros ingresados
media = suma / numeros

#Imprimo el resultado de la media 
print(f"La media de los numeros ingresados es: {media}")

"""Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

num = int(input("Ingrese un numero"))
num_invertido = 0

"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

#Pido al usuario ingresar un numero
numero = int(input("Ingresa un numero: "))

#Inicializo variable para luego guardar el numero invertido
numero_invertido = 0

#Bucle que se ejecuta si el numero es mayor a 0
while numero > 0:
    digito = numero % 10 #Con el operador modulo devuelvo el residuo de la division
    numero_invertido = numero_invertido * 10 + digito #Se agrega el numero al numero invertido
    #Eliminamos el ultimo digito del número 
    numero = numero // 10

# Mostramos el numero invertido
print("Número invertido:", numero_invertido)

