import pytube, os, subprocess

class MoveAround:
    
    #Función para seleccionar la ruta de la carpeta donde se almacenará la canción a descargar
    def SelectDirToSave(ruta="."):
        print('\n Selecciona el directorio donde almacenaremos la canción / las canciones.')
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
                break
            else:
                print(f"{opcion} no es una carpeta. Intente nuevamente.")

    #Función para seleccionar el archivo txt donde deberán estar todos los enlaces (1 enlace por fila) de las 
    #Canciones a descargar
    def SelectFileTXT(ruta="."):
        print('\n Selecciona el directorio donde localizaremos el archivo .txt con los enlaces de las canciones.')
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


class Downloaders:

    class Download_YT:

        # Función para descargar una cación
        def linkDownload_YT(): 
            url = input("Introduce el link de la canción: ")
            try:
                destinationPath = MoveAround.SelectDirToSave()
                video = pytube.YouTube(url)
                video.streams.filter(only_audio=True).first().download(output_path=destinationPath)
                print('Descaga realizada con éxito')

            except :
                print(f"Error al descargar la canción")

        # DEscargar varias canciones a la vez
        def textFileDownload_YT():
            filePath = MoveAround.SelectFileTXT() # Indicamos donde esta el documento txt
            whereToSave = MoveAround.SelectDirToSave() # Indicamos el directorio donde guardaremos las canciones a descargar
            songsLinks = []
            try:
                with open(filePath, 'r') as archivo:
                # Paso 2: Leer el contenido del archivo línea por línea
                    for linea in archivo:
                        songsLinks.append(linea)
            except:
                print('El archivo seleccionado no esta en el formato correcto.')
            
            for link in songsLinks:
                video = pytube.YouTube(link)
                video.streams.filter(only_audio=True).first().download(output_path=whereToSave)
                print('Descaga realizada con éxito')

    class Download_Spfy:

        # Función para descargar una cación
        def linkDownload_Spfy():
            url = input("Introduce el link de la canción: ")
            try:
                destinationPath = MoveAround.SelectDirToSave()
                # Comando para descargar la canción con spotdl
                comando = f'python -m spotdl download {url} --output "{destinationPath}"'
            
            # Ejecutar el comando
                subprocess.run(comando)
                print('Descaga realizada con éxito')


            except subprocess.CalledProcessError as e:
                print(f"Error al descargar la canción: {e}")
            
        
        def textFileDownload_Spfy():
            filePath = MoveAround.SelectFileTXT() # Indicamos donde esta el documento txt
            whereToSave = MoveAround.SelectDirToSave() # Indicamos el directorio donde guardaremos las canciones a descargar
            songsLinks = []
            try:
                with open(filePath, 'r') as archivo:
                    for linea in archivo:
                        songsLinks.append(linea)
            except:
                print('El archivo seleccionado no esta en el formato correcto.')
            
            for link in songsLinks:
                com = f'python -m spotdl download {link} --output {whereToSave}'
                subprocess.run(com)
                print('Descaga realizada con éxito')
                


class Pages:

    def pageYT():
        while True:
            print('\n ############################# DOWNLOADER DE YOUTUBE #############################')
            print('\nQue vamos a realizar?\n 1) Descargar una canción\n 2) Descargar varias canciones\n 3) Volver al menú')
            selection = int(input('\n Numero: '))
            if selection == 1:
                Downloaders.Download_YT.linkDownload_YT()
            elif selection == 2:
                Downloaders.Download_YT.textFileDownload_YT()
            elif selection == 3:
                print('\nSaliendo...')
                break
            else:
                print('\nSelección errónea')

    def pageSpfy():
        while True:
            print('\n ############################# DOWNLOADER DE SPOTIFY #############################')
            print('\nQue vamos a realizar?\n 1) Descargar una canción\n 2) Descargar varias canciones\n 3) Volver al menú')
            selection = int(input('\n Numero: '))
            if selection == 1:
                Downloaders.Download_Spfy.linkDownload_Spfy()
            elif selection == 2:
                Downloaders.Download_Spfy.textFileDownload_Spfy()
            elif selection == 3:
                print('\n Saliendo...')
                break
            else:
                print('\n Selección errónea')


class Program:

    def __init__(self):
        print("\nBienvenido al mejor downloader de canciones de YT y Spotify!!")
        while True:
            print('\n############################# MENÚ ############################# ')
            print('\nQue vamos a realizar?\n 1) Descargar de YouTube\n 2) Descargar de Spotify\n 3) Salir')

            selection = int(input('\nNumero: '))
            if selection == 1:
                Pages.pageYT()
            elif selection == 2:
                Pages.pageSpfy()
            elif selection == 3:
                print('\nSaliendo...')
                break
            else:
                print('\nSelección errónea\n')

Program()

