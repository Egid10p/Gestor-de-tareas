# Definimos la función agragar
def agregar():
    # Importamos pandas
    import pandas as pd

    # Leemos el csv
    df = pd.read_csv("datos.csv")
    
    # Cambiamos nuestra respuesta si es que hay o no hay tareas en el csv
    if df.shape[0] <= 0:
        print("No tienes tareas guardadas")
    else:
        print(df)
    
    # Le pedimos al usuario que introdusca el nombre de la tarea que desea agragar   
    while True:
        nombre = input("Introduce un nombre para la tarea que deseas agragar: ")
        print(f"vas a agregar el nombre: {nombre}")
        # Le pedimos al usuario que se asegure de que todo esta bien
        while True:
            descicion = input("¿Quiere continuar? si no quiere continuar puede reescribir el nombre (S/n): ")
            if descicion.lower() == "s" or descicion.lower() == "n" or descicion == "":
                break
            else:
                print('Introduce "s" o "n"')
        if descicion.lower() == "s" or descicion == "":
            break
    # Le pedimos al usuario que introdusca una descripción
    while True:
        info = input(f"Introduce una descripción a la tarea: {nombre}: ")
        print(f"Vas a agregar esta descripción: {info} \nA la tarea: {nombre}")
        # Le pedimos al usuario que confirme la descripción
        while True:
            descicion = input("¿Quiere continuar? si no quiere continuar puede reescribir la descripción (S/n): ")
            if descicion.lower() == "s" or descicion.lower() == "n" or descicion == "":
                break
            else:
                print('Introduce "s" o "n"')
        if descicion.lower() == "s" or descicion == "":
            break
        
    # Creamos una nueva fila con el estado Incompleta
    nueva_fila = {'tarea': nombre, 'descripción': info, 'estado' : 'Incompleta'}
    
    # Agragamos la nueva fila al DataFrame
    df = df._append(nueva_fila, ignore_index=True)
    print(f"Estas son todas sus tareas")
    print(df)
    
    # Guardamos el DataFrame
    df.to_csv('datos.csv', index=False)
    