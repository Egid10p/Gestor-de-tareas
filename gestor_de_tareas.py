# Importando todos los modulos
import agregar_tareas as at
import quitar_tareas as qt
import completar_tarea as ct
while True:
    # Imprimiendo titulo
    print("""
       _____           _                   _        _                           
      / ____|         | |                 | |      | |                          
     | |  __  ___  ___| |_ ___  _ __    __| | ___  | |_ __ _ _ __ ___  __ _ ___ 
     | | |_ |/ _ \/ __| __/ _ \| '__|  / _` |/ _ \ | __/ _` | '__/ _ \/ _` / __|
     | |__| |  __/\__ \ || (_) | |    | (_| |  __/ | || (_| | | |  __/ (_| \__ \\
      \_____|\___||___/\__\___/|_|     \__,_|\___|  \__\__,_|_|  \___|\__,_|___/                                                                          
    """)
    print("\t\t\t(Gestor de tareas)")

    # Pidiendole al usuario que introdusca una opción
    while True:
        try:
            print("\n\nElija una de las siguientes funciones: ")
            print("1. Agregar tarea")
            print("2. Quitar tarea")
            print("3. Completar tarea")
            print("")
            eleccion = int(input("Introduce una de las opciones 3: "))
            if (eleccion > 0 and eleccion <= 3):
                break
            else:
                print("Por favor introduce un numero del 1 al 3")
        except ValueError:
            print("Por favor introduce un numero del 1 al 3")
    # Ejecutando lo que a seleccionado el usuario
    if eleccion == 1:
        at.agregar()
    elif eleccion == 2:
        qt.quitar()
    elif eleccion == 3:
        ct.completar()
    # Preguntandole al usuario si quiere volver a ejecutar el programa
    while True:
        eleccion = input("Quieres volver a ejecutar el programa (S/n): ")
        if eleccion.lower() == "s" or eleccion.lower() == "n" or eleccion == "":
            break
        else:
            print("Por favor introduce S o N")
    if eleccion.lower() == "n":
        break