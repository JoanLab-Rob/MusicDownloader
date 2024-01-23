import os, subprocess
from DownloadMusic_App import *




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

