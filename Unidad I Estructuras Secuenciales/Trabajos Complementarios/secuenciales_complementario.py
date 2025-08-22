#Ejercicio 1
"""Crea una variable llamada "numero1" y asígnale un número entero de tu elección."""

numero1 = 26
print(f"El numero asignado es {numero1}")


#Ejercicio 2
"""No borres la variable número uno y crea una variable llamada "numero2" asignándole
un número decimal de tu elección."""

numero2 = 9.20
print(f"El numero asignado es {numero2}")


#Ejercicio 3
"""Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2."""

suma = numero1 + numero2


#Ejercicio 4
"""Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para
#multiplicación y otra para división. Imprime estas variables"""

resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1/numero2

print(f"La suma de {numero1} y {numero2} es {suma} ")
print(f"La resta de {numero1} y {numero2} es {resta} ")
print(f"La multiplicacion de {numero1} y {numero2} es {multiplicacion} ")
print(f"La division de {numero1} y {numero2} es {division} ")


#Ejercicio 5
"""Crea una variable llamada "nombre" y asígnale tu nombre como valor."""

nombre = "Nico"
print(f"Hola {nombre}")


#Ejercicio 6
"""Crea una variable llamada "precio" y asígnale un valor decimal que represente el
precio de un artículo ficticio"""

precio = 19.99
print(f"El precio del producto es de ${precio}")

#Ejercicio 7
"""Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale
un valor decimal que represente el descuento aplicado al artículo. Por ejemplo, si le
quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al
100% y el valor 0 al 0%.."""

descuento = 0.50
print(f"El descuento es de ${descuento}")


#Ejercicio 8
"""Ahora, intenta calcular el precio final aplicando el descuento al precio original y
almacena el resultado en una variable llamada "precio_final". Para ello vas a tener que
aplicar la lógica de matemáticas."""

precio_final = precio * (1-descuento)

print(f"El precio final del producto es {precio_final}")


#Ejercicio 9
"""Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu
elección. Qué sea un string."""

cadena = "Trabajo practico complementario"
print(f"La cadena ingresada es: {cadena}")


#Ejercicio 10
"""Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas
a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de
Python."""

longitud = len(cadena)
print(f"La longitud de {cadena} es:", longitud)


#Ejercicio 11
"""Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y
conviértelo en número entero. Lo puedes hacer en la misma variable o en otra, da lo
mismo."""

precio = 149.99
precio_entero = int(precio)

print("Precio original:", precio)
print("Precio entero:", precio_entero)


#Ejercicio 12
"""Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas
en una tercera variable llamada "nombre_completo", el nombre y el apellido con un
espacio entre medio. Puedes usar libremente la forma de concatenación que quieras"""

nombre = "Exequiel" 
apellido = "Tur"
#Concatenación con comillas para dejar un espacio entre el nombre y apellido
nombre_completo = nombre + " " + apellido

print(f"El nombre  es", nombre)
print(f"El apellido es", apellido)
print(f"El nombre completo es", nombre_completo)


#Ejercicio 13
""" Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10."""

edad = 26
edad_incrementada = edad + 5
edad_disminuida = edad_incrementada - 10

print(f"La edad es: {edad}. Incrementada en 5 es: {edad_incrementada}, y disminuida en 10 es: {edad_disminuida}")


#Ejercicio 14
"""Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y
centímetros. Por ejemplo: 1.83. Multiplícala por 4 y luego divídela en 3."""

altura = 1.77
altura = (altura * 4)/3

print(f"La altura final es de ", altura)


#Ejercicio 15
"""Crea una variable que contenga tu nombre completamente en mayúsculas. Después
transfórmalo todo en minúsculas con algún método o función de Python."""

nombre_en_mayus = "NICOLAS"
#Se usa el metodo .lower() para transformar todas las letras en minuscula
nombre_en_minus = nombre_en_mayus.lower()

print(f"El nombre en mayusculas es: {nombre_en_mayus} y el nombre en minusculas es: {nombre_en_minus}")


#Ejercicio 16
"""Por último, con la variable con el nombre en mayúsculas, aplica un método parecido
para que se transforme todo en minúsculas excepto la primera letra."""

primera_letra_mayus = nombre_en_mayus.capitalize()

print(f"El resultado final es {primera_letra_mayus}")