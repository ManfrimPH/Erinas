from Client import Client
import shutil
import os

def start_system():
  if os.path.exists('musicas'):
    shutil.rmtree('musicas')


system = Client()
start_system()

while True:
  ascii_art = """
                                                                                                                                                 
                                                                                                                                                 
       00000000000000                                                                                                                             
       00000000000000000                                                                                                                          
       0000       00000000                                                                                                                        
       0000          000000 00000     000000     00000    000000000    00000000000000 00000000000000     000000000     00000 000000              
       0000             000 000000    000000     00000 00000000000000  00000000000000 00000000000000   0000000000000   0000000000000             
       0000              000 00000   00000000   00000 000000    000000        0000000         000000  000000    00000  000000   00000            
       0000              000  00000  00000000   00000 00000      00000       000000         000000   000000     000000 00000    00               
       0000            0000   00000 0000  0000 00000  0000000000000000    0000000         0000000    00000000000000000 00000                     
       0000         0000000    000000000  0000000001  00000             20000004        0000000      000000            00000                     
       00000     000000000     000000000   00000000    000000     0000 0000000        0000000         000000     0000  00000                     
       00000000000000000        0000000    00000000     00000000000000 000000000000000000000000000000  000000000000000 00000                     
       0000000000000            000000      000000        0000000000   00000000000000 000000000000000     000000000    00000                     
                                                                                                                                                 
                                                                                                                                                 
                                                                                                                                                 
                                                                                                                                                 
  """

  print(ascii_art)
  print('Bem-Vindo ao Dwezzer! O seu player de música\n\n')
  value = input('Escolha uma opção: \t\t \n \n ' \
                '1-Adicionar Músicas ' \
                '\n 2-Criar Playlist' \
                '\n 3-Adicionar Música à Playlist ' \
                '\n 4-Listar Músicas' \
                '\n 5-Listar Playlists' \
                '\n 6-Tocar Música' \
                '\n 7-Tocar Plalist \n 8-Sair\n\n')
  
  match(int(value)):
    case 1:
      name = input('Nome da música:')
      system.add_musics(name)
    case 2:
      name = input('Nome da playlist:')
      system.add_playlist(name)
    case 3:
      name = input('Nome da música:')
      name1 = input('Nome da playlist:')
      system.add_musics_in_playlist(name1, name)
    case 4:
      system.list_musics()
    case 5:
      system.list_playlist()
    case 6:
      name = input('Nome da música:')
      system.play_music(name)
    case 7:
      name = input('Nome da playlist:')
      system.play_playlist(name)
    case 8:
      break

  os.system('clear')  
