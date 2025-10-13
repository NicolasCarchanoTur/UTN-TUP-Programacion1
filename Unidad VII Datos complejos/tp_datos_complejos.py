#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("1) Diccionario actualizado con nuevas frutas:", precios_frutas)


#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print("2) Diccionario con precios actualizados:", precios_frutas)


#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.

frutas = list(precios_frutas.keys())
print("3) Lista de frutas:", frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = numero

consulta = input("Ingresá un nombre para buscar su número: ")
print(contactos.get(consulta, "No existe ese contacto."))


#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra

frase = input("Ingresá una frase: ").lower().split()
palabras_unicas = set(frase)
conteo = {palabra: frase.count(palabra) for palabra in palabras_unicas}
print("Palabras únicas:", palabras_unicas)
print("Frecuencia de cada palabra:", conteo)


#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

alumnos = {}
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingresá la nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio = {promedio:.2f}")


#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)

parcial1 = {1, 2, 3, 4}
parcial2 = {3, 4, 5, 6}
print("Ambos parciales:", parcial1 & parcial2)
print("Solo uno:", parcial1 ^ parcial2)
print("Al menos uno:", parcial1 | parcial2)


#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

stock = {'lapiz': 10, 'goma': 3}
producto = input("Ingresá el producto: ")
if producto in stock:
    agregar = int(input("Unidades a agregar: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Stock inicial del nuevo producto: "))
    stock[producto] = nuevo_stock
print("Stock actualizado:", stock)

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos
#Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ('lunes', '10:00'): 'Reunión',
    ('martes', '15:00'): 'Clase'
}
dia = input("Ingresá el día: ")
hora = input("Ingresá la hora: ")
print(agenda.get((dia, hora), "No hay actividad registrada en ese horario."))


#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.


paises = {'Argentina': 'Buenos Aires', 'Chile': 'Santiago', 'Uruguay': 'Montevideo'}
capitales = {capital: pais for pais, capital in paises.items()}
print("Nuevo diccionario (capitales → países):", capitales)
