import os, subprocess
from DownloadMusic_App import *



class Download_Spfy:

            # Función para descargar una cación de spotify
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



