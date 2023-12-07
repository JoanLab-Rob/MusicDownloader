"""
https://www.youtube.com/watch?v=6bDaAcIxZiU - KETA PAL NENE
https://www.youtube.com/watch?v=Iv6tgrQ0Srk - Deadly Guns - From The Underground (Rave Core)(Official Videoclip)
https://www.youtube.com/watch?v=u3QYGIPzyag&list=PL_rVqNEc7L6VyOFAfcEnMoCPTFV0_Nprv
https://www.youtube.com/watch?v=Qccjcwxb0D0
https://www.youtube.com/watch?v=tvN8IAxzZSo
https://www.youtube.com/watch?v=CZ5Ue_Fv1e0
https://www.youtube.com/watch?v=KE0iTpLqRZk
https://www.youtube.com/watch?v=kZQT1tEb_hU
https://www.youtube.com/watch?v=aLWAEQjYe2U
https://www.youtube.com/watch?v=uFPwRAZkBPY
https://www.youtube.com/watch?v=KEr4aRmShj4
https://www.youtube.com/watch?v=sx-9yKR_LVQ
https://www.youtube.com/watch?v=2NifU4IPVSw
https://www.youtube.com/watch?v=ZFspOYo8wWQ
https://www.youtube.com/watch?v=hUTGTflHTrE
https://www.youtube.com/watch?v=lDumH5kCvBc
https://www.youtube.com/watch?v=SEZrXlEAI2I
https://www.youtube.com/watch?v=sgC3Gw7MdCw
https://www.youtube.com/watch?v=4-ci73MQkBE
https://www.youtube.com/watch?v=5v30slei3wU
https://www.youtube.com/watch?v=FggcRN-as-s
https://www.youtube.com/watch?v=1QDqm9-joz4
https://www.youtube.com/watch?v=SE8GuluBtLQ
https://www.youtube.com/watch?v=yI5XisenNlU


"""



import pytube 

# Paso 1: Abrir el archivo en modo lectura ('r')
lista_s = []
nombre_archivo = "songs.txt"
with open(nombre_archivo, 'r') as archivo:
    # Paso 2: Leer el contenido del archivo línea por línea
    for linea in archivo:
        lista_s.append(linea)



# Paso 3: Cerrar el archivo (se hace automáticamente con 'with')
for i in lista_s:
    url = i
    video = pytube.YouTube(url)
    op = video.streams.filter(only_audio=True).first().download()


