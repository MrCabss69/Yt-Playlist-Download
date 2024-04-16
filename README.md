
# Youtube Playlist Downloader

This project allows you to download songs from **public** YouTube playlists in MP3 format and save them to a local folder. It uses the `pytube` library for downloading and `moviepy` for format conversion.

## Requirements

Before you begin, make sure you have Python installed on your system. Additionally, you will need to install the following libraries:

- pytube
- moviepy

You can install these dependencies with the following command:

```bash
pip install pytube moviepy
```

## Use

This script supports downloading from a single playlist, multiple playlists by specifying comma-separated IDs, or from a list of playlist IDs provided in a text file. Follow these steps to use the script:

1. Clone this repository locally.
```bash
git clone https://github.com/MrCabss69/Yt-Playlist-Download.git
```
1. Open a terminal or command line and navigate to the directory where the script is located.
```bash
cd  Yt-Playlist-Download
```
2. Run the script by providing the playlist ID(s) or the path to a text file containing playlist IDs. You can also specify the output directory where the MP3 files will be saved.

### Single Playlist
```bash
python3 download_playlist.py ID_1 --output output_directory
```

### Multiple Playlists
```bash
python3 download_playlist.py ID_1,ID_2 --output output_directory
```

### Playlists from Text File
```bash
python3 download_playlist.py playlists.txt --output output_directory
```

## Example
To download a single YouTube playlist and save the MP3 files to a specified folder:

```bash
python3 download_playlist.py ID_1 --output music_folder
```

Replace `ID_1`,`ID_2`  with the actual ID of the YouTube PUBLIC (this is a must) playlist you want to download. For multiple IDs or a file, adjust the input accordingly.