"""
Esta parte del codigo podemos indicar donde alamacenaremos las canciones que vayamos a descargar
"""
import os

class MoveAround:
        
        #Función para seleccionar la ruta de la carpeta donde se almacenará la canción a descargar
        def SelectDirToSave(ruta="."):
            print('\n Selecciona el directorio donde almacenaremos la canción / las canciones.')
            try:
                while True:
                    # Mostrar contenido de la carpeta actual
                    print(f"\nContenido de {ruta}:")
                    contenido = os.listdir(ruta)
                    for elemento in contenido:
                        print(elemento)

                    # Solicitar al usuario que ingrese una opción
                    opcion = input("\nIngrese el nombre de la carpeta o '..' para ir atras ('s' para seleccionar directorio o 'q' para salir): ")

                    # Verificar la opción del usuario
                    if opcion.lower() == 's':
                        return os.path.abspath(ruta)# Salir del bucle si el usuario elige salir
                    elif os.path.isdir(os.path.join(ruta, opcion)):
                        # Si la opción es una carpeta, cambiar a esa carpeta
                        ruta = os.path.join(ruta, opcion)
                    elif opcion.lower()=='q':
                        print('Saliendo...')
                        return opcion.lower()
                    else:
                        print(f"{opcion} no es una carpeta. Intente nuevamente.")
            except:
                print("Error al intentar acceder a los directorios para almacenar las canciones")



