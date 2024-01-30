# Youtube Playlist Downloader

<<<<<<< HEAD
Este proyecto permite descargar canciones de listas de reproducción públicas de YouTube en formato MP3 y guardarlas en una carpeta local. Utiliza la biblioteca `pytube` para la descarga y `moviepy` para la conversión de formato.
=======
Este proyecto permite descargar canciones de listas de reproducción **públicas** de YouTube en formato MP3 y guardarlas en una carpeta local. Utiliza la biblioteca `pytube` para la descarga y `moviepy` para la conversión de formato.
>>>>>>> 1c4dd90 (:))

## Requisitos

Antes de comenzar, asegúrate de tener Python instalado en tu sistema. Además, necesitarás instalar las siguientes bibliotecas:

- pytube
- moviepy

Puedes instalar estas dependencias con el siguiente comando:

```bash
pip install pytube moviepy
```

Por último, navega hasta la lista de reproducción que desees descargar, y copia el id de la playlist que deseas descargar (lo que aparece a la derecha de list=)




## Uso

Para utilizar este script, sigue los siguientes pasos:

1. Clona este repositorio en local.

2. Abre una terminal o línea de comandos.

3. Navega hasta el directorio donde se encuentra el script.

4. Ejecuta el script con el ID de la lista de reproducción de YouTube como argumento: 

```bash 
<<<<<<< HEAD
python3 download_playlist.py [ID de la lista de reproducción]
=======
python3 download_playlist.py playlist_id --output output_directory
>>>>>>> 1c4dd90 (:))
```

Reemplaza `[ID de la lista de reproducción]` con el ID real de la lista de reproducción de YouTube que deseas descargar.

## Ejemplo
```bash
<<<<<<< HEAD
python3 download_playlist.py PLAYLIST_ID --output PLAYLIST_NAME
=======
python3 download_playlist.py playlist_id --output output_directory
>>>>>>> 1c4dd90 (:))
```
