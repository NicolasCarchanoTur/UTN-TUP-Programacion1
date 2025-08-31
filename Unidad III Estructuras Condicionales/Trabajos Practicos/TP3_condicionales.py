from statistics import mode, median, mean
import random

"""1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""

#Pide al usuario que ingrese la edad
edad = int(input("Ingresa tu edad: "))

#Si el usuario es mayor de 18 imprimira que es mayor de edad, sino no mostrara nada
if edad > 18:
    print("Es mayor de edad")

"""2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”."""

#Pide al usuario que ingrese la nota
nota = int(input("Ingrese su nota: "))

#Estrucura if-else para comprobar la nota e imprimir aprobado o desaprobado
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

"""3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar."""

#Pide al usuario que ingrese un numero par
num = int(input("Ingrese un numero par: "))

#Estructura if-else para verificar si el numero ingresado por el usuario es MOD 0 
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un numero par")

"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años."""

#Pide al usuario que ingrese la edad
edad = int(input("Ingrese su edad: "))

#Estrucura if-elif-else 
if edad < 12:
    print("Nino/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto")

"""5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string."""

#Pide al usuario ingresaer una contrasena entre 8 y 14 caracteres
contrasena = str(input("Ingrese una contrasena entre 8 y 14 caracteres: "))

#Verifica que la contrasena cumpla la condicion
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
#Si no cumple, muestra por pantalla nuevamente la condicion
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

"""6) Escribir un programa que tome la lista numeros_aleatorios, 
calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla."""

#Crea lista de 50 numeros aleatorios entre el 1 y el 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(f"{numeros_aleatorios}")

#Guardo en las variables los resultados de los parametros estadisticos
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

#Imprimo por pantalla los resultados
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

#Comparo los resultados para determinar el sesgo
if media > mediana > moda:
    sesgo = "Positivo o a la derecha"
elif media < mediana < moda:
    sesgo = "Negativo o a la izquierda"
else:
    sesgo = "Sin sesgo"

print(f"{sesgo}")

"""7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla."""

#Solicito una frase o palabra al usuario
cadena = str(input("Ingresa una palabra o frase: "))

#Verificar si el último carácter es una vocal
if cadena[-1].lower() in 'aeiou':
#Añadir el signo de exclamación si se cumple la condicion
    cadena += "!"  

#Imprimir el resultado
print(cadena)

"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas."""

nombre = str(input("Ingrese su nombre: "))
opcion = int(input("Ingrese la opcion que desee siendo: 1-Nombre en mayuscula / 2-Nombre en minusculas / 3-Nombre con primera letra en mayusculas "))

if opcion == 1:
    nombre = nombre.upper()
elif opcion == 2:
    nombre = nombre.lower()
else:
    nombre == nombre.title()

print(nombre)

"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."""

magnitud = float(input("Ingrese la magnitud del terremoto en escala de Richter: "))

if magnitud < 3:
    print("Muy leve.")
elif magnitud >= 3 and magnitud < 4:
    print("Leve. Ligeramente perceptible.")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado. Sentido por personas pero generalmente no causa danos.")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte. Puede causar danos en estructuras debiles.")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte. Puede causar danos significativos.")
else:
    print("Extremo. Puede causar danos a gran escala.")

"""10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano."""

#Pedirle al usuario que ingrese el hemisferio, mes y dia 
hemisferio = str(input("Ingrese el hemisferio donde se encuentra siendo: 'N' para hemisferio norte / 'S' para hemisferio sur: "))
mes = int(input("Ingrese el mes del ano (01-12): "))
dia = int(input("Ingrese el dia del mes (01-31): "))

#Estructura if-elif para determinar que estacion segun el hemisferio y fecha ingresada
if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    hemisferio_norte = "Invierno"
    hemisferio_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    hemisferio_norte = "Primavera"
    hemisferio_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    hemisferio_norte = "Verano"
    hemisferio_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    hemisferio_norte = "Otoño"
    hemisferio_sur = "Primavera"

#Mostrar la estacion segun el hemisferio
if hemisferio == "N":
    print(f"En el hemisferio norte es {hemisferio_norte}.")
elif hemisferio == "S":
    print(f"En el hemisferio sur es {hemisferio_sur}.")
else:
    print("No es una opcion valida")