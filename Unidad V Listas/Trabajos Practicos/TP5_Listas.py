"""1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range."""

#Creo lista del 4 al 100 con paso 4
multiplos = list(range(4, 101, 4))
#Imprimo lista
print(multiplos)

"""2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos!"""

#Creo lista elementos
elementos = ["Mouse" , "Teclado" , "Pantalla" , "Auriculares" , "Mousepad"]
#Con indice negativo recorro la lista desde atras e imprimo el penultimo elemento
print(elementos[-2])

"""3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla."""

#Creo lista vacia
palabras = []

#Agrego elementos con el metodo append
palabras.append("manzana")
palabras.append("banana")
palabras.append("cereza")

#Imprimo la lista
print(palabras)

"""4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos!"""

#Creo lista animales
animales = ["perro", "gato", "conejo", "pez"]

#Con los indices reemplazo los elementos que ya estaban en esa posicion
animales[1] = "loro"
animales[-1] = "oso"

#Imprimo la lista con los nuevos elementos
print(animales)


"""5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza."""

#Creo lista numeros
numeros = [8, 15, 3, 22, 7]

#Con remove y max remuevo el numero mayor de la lista
numeros.remove(max(numeros))

#Imprimo la lista
print(numeros)
#Este codigo remueve el numero maximo de la lista, ya que al reemplazar el 3 por un 33 removio ese numero en vez del 22

"""6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros."""

#Creo lista que recorre del 10 al 30 con paso 5
numeros = list(range(10, 31, 5))

#Imprimo los numeros en la posicion 0 y 1
print(numeros[0])
print(numeros[1])

"""7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera."""

#Creo lista autos
autos = ["sedan", "polo", "suran", "gol"]

#Reemplazo la posicion 1 y 2 de la lista
autos[1] = "taos"
autos[2] = "nivus"

#Imprimo la nueva lista
print(autos)

"""8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla."""

#Creo lista vacia 
dobles = []

#Con el metodo append agrego el resultado de la operacion
dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)

#Imprimo la lista
print(dobles)

"""9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla"""

#Se crea una lista anidada
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

#En la tercera lista agrego jugo al final
compras[2].append("jugo")
#En la segunda lista, reemplazo el elemento de la posicion 1 que es fideos por tallarines
compras[1][1] = "tallarines"
#En la primer lista, con el metodo .remove , elimino el elemento pan
compras[0].remove("pan")

#Imprimo la nieva lista
print(compras)

"""10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla."""

#Se crea lista anidada 
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

#Imprimo la lista
print(lista_anidada)