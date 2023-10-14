# Definimos la función completar
def completar():
    # Importamos pandas
    import pandas as pd

    # Leemos el csv
    df = pd.read_csv("datos.csv")
    columna = "estado"
    # Nos preguntamos si hay tareas en el Dataframe
    if df.shape[0] <= 0: # Si no hay tareas no podra ejecutar el programa
        print("No tienes ninguna tarea, agraga una tarea para poder completarla")
    else:
        print(df)
        print("")
        # Le pedimos al usuario que introdusca el numero indece de la tarea que desea completar
        while True:
            try:
                fila = int(input("Introduce el numero indice de la tarea que deseas completar: "))
                if fila < df.shape[0] and fila >= 0:
                    break
                else:
                    print(f"Por favor introduce un numero de 0 al {df.shape[0]-1}")
            except ValueError:
                print(f"Por favor introduce un numero de 0 al {df.shape[0]-1}")
        # Le pedimos al usuario que se asegure de que todo esta bien
        while True:
            decición = input(f"Estas apunto de completar la tarea: \n\n{df.iloc[fila]} \n\nEstas seguro de esta acción (S/n): ")
            if decición.lower() == "s" or decición.lower() == "n" or decición == "":
                break
            else:
                print("Error: introduce S o N")
        # Verificamos la respuesta y si es igual "s" o es un elemento vacio completamos la tarea
        if decición.lower() == "s" or decición == "":
            # Cambiamos el estado de la tarea a completa
            df.iloc[fila, df.columns.get_loc(columna)] = 'Completa'
            # Mostramos el df en pantalla y guardamos en el csv
            print(df)
            df.to_csv("datos.csv", index=False)