import random

""""Vas a programar un juego clásico contra la computadora: Piedra, papel o tijeras.
Reglas:
1. El programa debe mostrar un menú con las opciones:
o Piedra
o Papel
o Tijera
2. El jugador elegirá una opción.
3. La computadora elegirá su jugada al azar.
4. El programa debe comparar ambas jugadas y mostrar quién gana:
o Piedra vence a Tijera.
o Tijera vence a Papel.
o Papel vence a Piedra.
o Si ambos eligen lo mismo, es empate.
Extra:
• Llevar un marcador de cuántas partidas gana el jugador y cuántas la computadora.
• El juego termina cuando el jugador elija salir, mostrando el resultado final.
"""

#Inicializo contadores en 0
contador_jugador = 0
contador_pc = 0

print("PIEDRA, PAPEL O TIJERA")

#Bucle while que se ejecuta hasta que el jugador elija salir
while True:
    #Imprimo menu de opciones
    print("1-Piedra")
    print("2-Papel")
    print("3-Tijera")
    print("4-Salir")

    #Jugador ingresa una opcion
    opcion_jugador = int(input("Elige una opcion: "))

    #Verifico si el jugador eligio salir
    if opcion_jugador == 4:
        print("Saliste del juego!")
        break

    #Verifico si el jugador ingreso una opcion invalida
    if opcion_jugador < 1 or opcion_jugador > 4:
        print("Opcion invalida, intenta de nuevo.")
        continue
    
    #Numero random entre 1 y 3 que se le asigna a la pc
    opcion_pc = random.randint(1, 3)

    #Se muestra mensaje de la opcion elegida por el jugador
    if opcion_jugador == 1:
        print("Elegiste: Piedra")
    elif opcion_jugador == 2:
        print("Elegiste: Papel")
    elif opcion_jugador == 3:
        print("Elegiste: Tijera")

    #Se muestra mensaje de la opcion asignada a la pc
    if opcion_pc == 1:
        print("La computadora eligio: Piedra")
    elif opcion_pc == 2:
        print("La computadora eligio: Papel")
    elif opcion_pc == 3:
        print("La computadora eligio: Tijera")

    #Comparaciones entre la opcion que eligio el usuario y la dada a la pc aleatoriamente
    if opcion_jugador == opcion_pc:
        print("Empate")
    elif (opcion_jugador == 1 and opcion_pc == 3) or (opcion_jugador == 2 and opcion_pc == 1) or (opcion_jugador == 3 and opcion_pc == 2):
        print("Ganaste esta ronda!")
        contador_jugador += 1
    else:
        print("La computadora gana esta ronda!")
        contador_pc += 1

#Imprimo las veces que gano el jugador
print(f"Veces que gano el jugador: {contador_jugador}")
#Imprimo las veces que gano la pc
print(f"Veces que gano la computadora: {contador_pc}")
