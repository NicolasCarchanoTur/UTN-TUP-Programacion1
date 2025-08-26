#solicitar al usuario que ingrese la fecha actual en formato “día, DD/MM”

fecha = input("Ingrese la fecha en formato 'dia, DD/MM': ")

#Se usa .split(",") para separar el texto en dos partes
dia_escrito, fecha_num = fecha.split(",")
#Se usa .strip() para quitar espacios de sobra y .lower() para transformar todo el string en minusculas
dia_escrito = dia_escrito.strip().lower()
dia, mes = fecha_num.strip().split("/")
dia = int(dia)
mes = int(mes)

#Se imprime el dia ingresado
print(f"El dia es {dia_escrito}, {dia}/{mes}")

#Se comprueba que las fechas ingresadas esten dentro de lo valido
if dia < 1 or dia >31 or mes < 1 or mes > 12:
    print("La fecha ingresada no es valida")

#Se le asigna segun el dia ingresado, el nivel de ese dia
if dia_escrito == "lunes":
    nivel = "inicial"
elif dia_escrito == "martes":
    nivel = "intermedio"
elif dia_escrito == "miercoles":
    nivel = "avanzado"
elif dia_escrito == "jueves":
    nivel = "practica hablada"
elif dia_escrito == "viernes":
    nivel = "viajeros"
else:
    nivel = None

#Si ningun dia ingresado es valido se imprime un error, si es un dia valido imprime que nivel se va a dictar
if nivel is None:
    print("Error: día de la semana invalido.")
else:
    print(f"Hoy se dicta el nivel: {nivel}")

#Si en el if anterior se imprime inicial, intermedio o avanzado, pregunta si hubo examenes
if nivel in ["inicial", "intermedio", "avanzado"]:
    examenes = input("¿Hoy hubo examenes? (si/no): ").lower()
#Si es si, se debe ingresar la cantidad de aprobados y desaprobados para sumarlos y obtener un porcentaje
    if examenes == "si":
        aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
        desaprobados = int(input("Ingrese la cantidad de alumnos desaprobados: "))
        total = aprobados + desaprobados
        if total > 0:
            porcentaje = (aprobados / total) * 100
            print(f"El porcentaje de aprobados es: {porcentaje:.2f}%")
        else:
            print("No se registraron alumos")
    else:
        print("Hoy no hubo examen")
#Si el nivel es practica hablada se pide que se ingrese el porcentaje de asistencia y si es > 50% se imprime que asistio la mayoria, si no, no asistio la mayoria
elif nivel == "practica hablada":
    asistencia = float(input("Ingrese el porcentaje de asistencia: "))
    if asistencia > 50:
        print("Asistio la mayoria")
    else:
        print("No asistio la mayoria")
#Si el nivel es viajeros y es el dia 1 del mes 1 o del mes 7 entonces se pide cantidad de alumnos y el arancel para imprimir el ingreso total
elif nivel == "viajeros":
    if dia == 1 and (mes == 1 or mes == 7):
        print("Comienzo de nuevo ciclo")
        alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel = float(input("Ingrese el arancel en $ por alumno: "))
        ingreso = alumnos * arancel
        print(f"Ingreso total: ${ingreso:.2f}")
    else:
        print("Clase regular de ingles para viajeros")

