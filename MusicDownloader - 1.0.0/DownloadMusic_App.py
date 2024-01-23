import pytube, os, subprocess, spotdl

class App:

    def __init__():
        
        if os.name == 'posix':  # Linux
            clean = "clear"
            command = True
            
        else:
            clean = "cls"
            command = False

        return clean, command
    clean,command = __init__() 

     
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

    class Downloaders:

        class Download_YT:

            # Función para descargar una cación
            def linkDownload_YT(): 
                os.system(App.clean)
                url = input("Introduce el link de la canción: ")
                try:
                    destinationPath = App.MoveAround.SelectDirToSave()
                    if destinationPath.lower() != 'q':
                        video = pytube.YouTube(url)
                        #                                                 sin la opción "filename" la cancion se descarga en mp4 pero sin video
                        video.streams.filter(only_audio=True).first().download(filename=f"{video.title}.mp3",output_path=destinationPath)
                        print('Descarga realizada con éxito')

                except :
                    print(f"Error al descargar la canción")

            # Descargar varias canciones a la vez
            def PlaylistDownload_YT():
                try:
                    linkPlaylist = input(f"Introduce el link de la playlist de YT y asegurate que está publica: ")
                    whereToSave = App.MoveAround.SelectDirToSave() # Indicamos el directorio donde guardaremos las canciones a descargar

                    if whereToSave.lower() != 'q':
                        videos = pytube.Playlist(linkPlaylist)
                        for video in videos.videos:
                            print(f"Descargando: {video}")
                            video.streams.filter(only_audio=True).first().download(filename=f"{video.title}.mp3",output_path = whereToSave)
                    
                except:
                    print("Ha ocurrido un error")
        class Download_Spfy:

            # Función para descargar una cación
            def linkDownload_Spfy():
                os.system(App.clean)
                url = input("Introduce el link de la canción: ")
                try:
                    destinationPath = App.MoveAround.SelectDirToSave()
                    destinationPath2 = destinationPath.replace(' ', '\ ')
                    if destinationPath.lower() != 'q':
                        if App.command:
                            comando = f'python -m spotdl download {url} --output {destinationPath2}' # Linux
                        else:
                            comando = f'python -m spotdl download {url} --output "{destinationPath}"'

                        try:
                            os.system(comando)
                        except:
                            subprocess.run(comando)

                        
                    
                except os.error as e:
                    print(f"Error al descargar la canción: {e}")
                
            
            # Función para descargar más de una cación de spotify (lista)
            def PlaylistDownload_Spfy():
                os.system(App.clean)
                url = input("Introduce el link de la playlist de Spotify y asegurate que está publica: ")
                try:
                    destinationPath = App.MoveAround.SelectDirToSave()
                    destinationPath2 = destinationPath.replace(' ', '\ ')
                    if destinationPath != 'q':
                        if os.name == 'posix':
                            comando = f'python -m spotdl download {url} --output {destinationPath2}'
                        else:
                            comando = f'python -m spotdl download {url} --output "{destinationPath}"'

                        
                        try:
                            os.system(comando)
                        except:
                            subprocess.run(comando)
                    
                except subprocess.CalledProcessError as e:
                    print(f"Error al descargar la canción: {e}")


    class Pages:

        def pageYT():
            while True:
                os.system(App.clean)
                print('\n############################# DOWNLOADER DE YOUTUBE #############################')
                print('\nQue vamos a realizar?\n 1) Descargar una canción\n 2) Descargar varias canciones\n 3) Volver al menú')
                selection = int(input('\nNumero: '))
                if selection == 1:
                    App.Downloaders.Download_YT.linkDownload_YT()
                elif selection == 2:
                    App.Downloaders.Download_YT.PlaylistDownload_YT()
                elif selection == 3:
                    print('\nSaliendo...')
                    break
                else:
                    print('\nSelección errónea')

        def pageSpfy():
            while True:
                os.system(App.clean)
                print('\n############################# DOWNLOADER DE SPOTIFY #############################')
                print('\nQue vamos a realizar?\n 1) Descargar una canción\n 2) Descargar varias canciones\n 3) Volver al menú')
                selection = int(input('\nNumero: '))
                if selection == 1:
                    App.Downloaders.Download_Spfy.linkDownload_Spfy()
                elif selection == 2:
                    App.Downloaders.Download_Spfy.PlaylistDownload_Spfy()
                elif selection == 3:
                    print('\nSaliendo...')
                    break
                else:
                    print('\nSelección errónea')


    class Program:

        def launcher():
            while True:
                os.system(App.clean)
                print('\n############################# MENÚ #############################')
                print('\nQue vamos a realizar?\n 1) Descargar de YouTube\n 2) Descargar de Spotify\n 3) Salir')

                selection = int(input('\nNumero: '))
                if selection == 1:
                    App.Pages.pageYT()
                elif selection == 2:
                    App.Pages.pageSpfy()
                elif selection == 3:
                    print('\nSaliendo...')
                    break
                else:
                    print('\nSelección errónea\n')

try:
    App.Program.launcher()
except:
    print("Ha ocurrido un error al iniciar el programa, por favor compruebe que tiene instalado los requirements.txt y vuelva a intentarlo. Si el error persiste",
          "ponganse en contacto con nosotros")
