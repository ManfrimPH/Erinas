from Client import Client
import shutil
import os

def start_system():
  if os.path.exists('musicas'):
    shutil.rmtree('musicas')


system = Client()
start_system()

while True:

  value = input('Escolha uma das opções: \t\t \n ' \
                '1-Adicionar Musicas ' \
                '\n 2-Adicionar Playlist' \
                '\n 3-Adicionar Musicas a Playlist ' \
                '\n 4-Listar Musicas' \
                '\n 5-Listar Playlist' \
                '\n 6-Tocar Musica' \
                '\n 7-Tocar Plalist \n 8-Sair\n\n')
  
  match(int(value)):
    case 1:
      name = input('Nome da musica:')
      system.add_musics(name)
    case 2:
      name = input('Nome da playlist:')
      system.add_playlist(name)
    case 3:
      name = input('Nome da musica:')
      name1 = input('Nome da playlist:')
      system.add_musics_in_playlist(name1, name)
    case 4:
      system.list_musics()
    case 5:
      system.list_playlist()
    case 6:
      name = input('Nome da musica:')
      system.play_music(name)
    case 7:
      name = input('Nome da playlist:')
      system.play_playlist(name)
    case 8:
      break
