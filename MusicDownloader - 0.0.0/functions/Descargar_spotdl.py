import subprocess, MoveOnPC

def descargar_cancion_spotify(url_cancion):
    try:
        ruta_destino = MoveOnPC.explore_files()
        # Comando para descargar la canción con spotdl
        comando = f'python -m spotdl download {url_cancion} --output "{ruta_destino}"'
        
        # Ejecutar el comando
        subprocess.run(comando, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al descargar la canción: {e}")

if __name__ == "__main__":
    # URL de la canción de Spotify
    url_cancion_spotify = "https://open.spotify.com/intl-es/track/1dJhW3HRdLnySFEUhf6VRh?si=4bb52b91ef754ba6"  # Reemplaza con la URL de la canción
    
    # Descargar la canción
    descargar_cancion_spotify(url_cancion_spotify)

