import archivos as a

while True:
    print("Gestor de Productos")
    print("1-Mostrar productos")
    print("2-Agregar producto")
    print("3-Buscar producto")
    print("4-Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        a.mostrar_productos()
    elif opcion == "2":
        a.agregar_producto()
    elif opcion == "3":
        productos = a.cargar_productos_en_lista()
        a.buscar_producto(productos)
    elif opcion == "4":
        print("Salir del programa")
        break
    else:
        print("No ingreso una opcion valida. Intente nuevamente")

