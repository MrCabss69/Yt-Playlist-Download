import os
import argparse
from pytube import Playlist
from moviepy.editor import AudioFileClip

def download_and_convert(playlist_url, output_directory):

    pl = Playlist(playlist_url)
    for video in pl.videos:
        try:
            # Descarga el stream de audio
            audio_stream = video.streams.filter(only_audio=True).first()
            audio_file = audio_stream.download(output_path=output_directory)

            # Nombre del archivo final
            final_file = os.path.splitext(audio_file)[0] + '.mp3'

            # Convertir el archivo a MP3
            with AudioFileClip(audio_file) as audio_clip:
                audio_clip.write_audiofile(final_file)

            # Eliminar el archivo original descargado
            os.remove(audio_file)

            print(f'Descargado y convertido: {video.title}')
        except Exception as e:
            print(f'Error al descargar o convertir {video.title}: {e}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Descarga y convierte vídeos de YouTube a MP3.')
    parser.add_argument('playlist_id', help='ID de la lista de reproducción de YouTube')
    parser.add_argument('--output', help='Directorio de salida para los archivos MP3')
    args = parser.parse_args()
    playlist_url = f'https://www.youtube.com/playlist?list={args.playlist_id}'
    download_and_convert(playlist_url, args.output)
