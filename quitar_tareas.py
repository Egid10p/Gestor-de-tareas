# Definimos la función quitar
def quitar():
    # Importamos pandas
    import pandas as pd

    # Leemos el csv
    df = pd.read_csv("datos.csv")
    
    # Verificamos que haya tareas y si no hay tareas no podra ejecutar el programa y se le mostrara un mensaje
    if df.shape[0] <= 0:
        print("No tienes ninguna tarea, agraga una tarea para poder borrarla")
    else:
        print(df)
        # Le pedimos al usuario que elija tarea por su numero indice
        while True:
            try:
                fila = int(input("Introduce el numero indicie de la tarea que deseas eliminar: "))
                print("\n")
                if fila < df.shape[0] and fila >= 0:
                    break
                else:
                    print(f"Introduce un numero del 0 al {df.shape[0]-1}")
            except ValueError:
                print("Introduce un numero")
        
        # Le informamos al usuario las consecuencias de esta acción y le pedimos su confirmación
        while True:
            decición = input(f"Estas apunto de eliminar la tarea: \n\n{df.iloc[fila]} \n\nEsta acción no se puede revertir\nEstas seguro de esta acción (s/N): ")
            if decición.lower() == "s" or decición.lower() == "n" or decición == "":
                break
            else:
                print("Error: introduce S o N")
        # Solo si la respuesta es igual a "s" vamos a borrar la tarea
        if decición.lower() == "s":
            df.drop(fila)
            df.to_csv("datos.csv", index=False)
            print(df)
        else:
            print("Usted no eliminara la tarea")

