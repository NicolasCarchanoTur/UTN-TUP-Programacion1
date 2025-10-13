import math

#1
def imprimir_hola_mundo():
    print("Hola Mundo")

#2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

#3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#4
def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

#5
def segundos_a_horas(segundos):
    return segundos / 3600   # 1 hora = 3600 segundos

#6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

#7
def operaciones_basicas(a, b):
    print(f"La suma de {a} mas {b} es igual a {a+b}")
    print(f"La resta de {a} menos {b} es igual a {a-b}")
    print(f"La multiplicacion de {a} por {b} es igual a {a*b}")
    print(f"La division de {a} dividido {b} es igual a {a/b}")

#8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)



"""1. Crear una función llamada imprimir_hola_mundo que imprima por3
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""

imprimir_hola_mundo()

"""2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""

nombre_ingresado = input("Ingrese su nombre: ")
print(saludar_usuario(nombre_ingresado))

"""3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
Pedir los datos al usuario y llamar a esta función con los valores ingresados."""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro 
y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio 
como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario 
y llamar ambas funciones para mostrar los resultados."""

radio = float(input("Ingrese el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y 
mostrar el resultado usando esta función."""

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)

print(f"{segundos} segundos equivalen a {horas:.2f} horas.")


"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función."""

numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)

"""7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara."""

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

"""8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales."""

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")




