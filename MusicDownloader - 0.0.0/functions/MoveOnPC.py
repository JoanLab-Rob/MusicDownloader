"""
Este documento nos permite movernos a traves de las carpetas para indicar el directorio donde almacenaremos
las canciones descargadas
"""


import os

def explore_files(ruta="."):
    while True:
        # Mostrar contenido de la carpeta actual
        print(f"\nContenido de {ruta}:")
        contenido = os.listdir(ruta)
        for elemento in contenido:
            print(elemento)

        # Solicitar al usuario que ingrese una opción
        opcion = input("\nIngrese el nombre de la carpeta o '..' para ir atras ('s' para seleccionar directorio): ")

        # Verificar la opción del usuario
        if opcion.lower() == 's':
            return os.path.abspath(ruta)# Salir del bucle si el usuario elige salir
        elif os.path.isdir(os.path.join(ruta, opcion)):
            # Si la opción es una carpeta, cambiar a esa carpeta
            ruta = os.path.join(ruta, opcion)
        else:
            print(f"{opcion} no es una carpeta. Intente nuevamente.")

if __name__ == "__main__":
    # Comenzar exploración desde el directorio actual
    print(explore_files())
