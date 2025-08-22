#Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo")

#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = input("Ingresa tu nombre:")
print(f"Hola {nombre}!")

#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingresa tu nombre:")
apellido = input("Ingresa tu apellido:")
edad = input("Ingresa tu edad:")
residencia = input("Ingresa tu residencia:")
print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")

#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

import math

radio = float(input("Ingresa el radio del círculo: "))

area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos = int(input("Ingrese cantidad de segundos"))
horas = segundos / 3600
print(f"La cantidad de segundos equivale a {horas} horas")

#Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero = int(input("Ingrese un numero para multiplicar"))
for i in range(1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos

numero_uno = int(input("Ingrese el primer numero: "))
numero_dos = int(input("Ingrese el segundo numero: "))

suma = numero_uno + numero_dos
resta = numero_uno - numero_dos
multiplicacion = numero_uno * numero_dos
division = numero_uno / numero_dos

print(f"La suma de {numero_uno} + {numero_dos} es: {suma}")
print(f"La resta de {numero_uno} - {numero_dos} es: {resta}")
print(f"La multiplicacion de {numero_uno} * {numero_dos} es: {multiplicacion}")
print(f"La division de {numero_uno} / {numero_dos} es: {division} ")

#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal.  

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)

print(f"El indice de masa corporal es de {imc}")

#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit

temperatura_en_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_en_fahrenheit = (9/5 * temperatura_en_celsius) + 32

print(f"{temperatura_en_celsius} grados celsius son {temperatura_en_fahrenheit} grados fahrenheit")

#Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

nota_1 = float(input("Ingresa la primer nota: "))
nota_2 = float(input("Ingresa la seguna nota: "))
nota_3 = float(input("Ingresa la tercer nota: "))

promedio = float((nota_1 + nota_2 + nota_3)/3)

print(f"El promedio de {nota_1} + {nota_2} + {nota_3} es de {promedio}")
