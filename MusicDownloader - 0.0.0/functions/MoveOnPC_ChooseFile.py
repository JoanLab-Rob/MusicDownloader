import os

def explore_and_select(ruta="."):
    while True:
        # Mostrar contenido de la carpeta actual
        print(f"\nContenido de {ruta}:")
        contenido = os.listdir(ruta)
        for elemento in contenido:
            print(elemento)

        # Solicitar al usuario que ingrese una opción
        opcion = input("\nIngrese el nombre de la carpeta o '..' para ir atrás ('s' para seleccionar directorio, 'q' para salir): ")

        # Verificar la opción del usuario
        if opcion.lower() == 's':
            fileName =  input("\nIngrese el nombre del archivo .txt con los enlaces de las canciones: ")
            archivo_seleccionado = os.path.abspath(ruta)+'\\'+ fileName
            if os.path.isfile(archivo_seleccionado):
                return os.path.abspath(archivo_seleccionado)
            else:
                print("La ruta ingresada no es un archivo válido. Intente nuevamente.")
        elif opcion.lower() == 'q':
            return os.path.abspath(ruta)  # Salir del bucle devolviendo la ruta actual
        elif os.path.isdir(os.path.join(ruta, opcion)):
            # Si la opción es una carpeta, cambiar a esa carpeta
            ruta = os.path.join(ruta, opcion)
        else:
            print(f"{opcion} no es una carpeta. Intente nuevamente.")

if __name__ == "__main__":
    # Ejemplo de cómo utilizar la función combinada
    archivo_o_carpeta = explore_and_select()
    
    if archivo_o_carpeta:
        print(f"Archivo o carpeta seleccionada: {archivo_o_carpeta}")
        # Aquí puedes realizar otras operaciones según sea necesario
    else:
        print("Operación cancelada por el usuario.")
