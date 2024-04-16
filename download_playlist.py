import os
import argparse
from pytube import Playlist
from moviepy.editor import AudioFileClip

def download_and_convert(playlist_url, output_directory):
    try:
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
    except Exception as e:
        print(f'Error al procesar la playlist {playlist_url}: {e}')

def process_input(input_value, output_directory):
    if os.path.isfile(input_value):
        with open(input_value, 'r') as file:
            playlist_ids = [line.strip() for line in file]
    else:
        playlist_ids = [id.strip() for id in input_value.split(',')]

    for playlist_id in playlist_ids:
        playlist_url = f'https://www.youtube.com/playlist?list={playlist_id}'
        download_and_convert(playlist_url, output_directory)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Descarga y convierte vídeos de YouTube a MP3.')
    parser.add_argument('input', help='ID de lista de reproducción, lista de IDs separada por comas, o archivo de texto con IDs.')
    parser.add_argument('--output', help='Directorio de salida para los archivos MP3', default='./')
    args = parser.parse_args()
    
    # Procesar los inputs y manejar los errores adecuadamente
    try:
        process_input(args.input, args.output)
    except Exception as e:
        print(f'Error al procesar el input: {e}')
