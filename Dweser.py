import yt_dlp #type: ignore
import pygame #type: ignore

def dowload(nome_musica):
    info_musica = {}

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'musicas/{nome_musica}.%(ext)s',
        'quiet': True,
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'default_search': 'ytsearch1',
        'extract_flat': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f'Buscando e baixando: {nome_musica}')
        result = ydl.extract_info(nome_musica, download=True)

        if 'entries' in result:
            result = result['entries'][0]

        info_musica = {
            'nome_musica_usuario' : nome_musica,
            'titulo': result.get('title'),
            'canal': result.get('uploader'),
            'duracao_segundos': result.get('duration'),
        }

    return info_musica

def play(nome_musica):
    pygame.mixer.init()
    pygame.mixer.music.load(f"musicas/{nome_musica}.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
