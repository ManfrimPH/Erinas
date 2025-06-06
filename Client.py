from AVLTree import AVLTree
from Dweser import dowload, play

class Client:

  def __init__(self):
    self.tree = AVLTree()
    self.raiz = None
    self.musicas : dict = {}

  def add_musics(self, name: str):
    inf = dowload(nome_musica=name)
    self.musicas[inf['titulo']] = inf

  def add_playlist(self, name_playlist):
    self.raiz = self.tree.insert(self.raiz,{name_playlist : []})

  def add_musics_in_playlist(self, name_playlist, name_music):
    
    temp = self.tree.search(self.raiz,name_playlist)
    if temp.get(name_playlist):
      temp[name_playlist].append(self.musicas.get(name_music, []))
      new_musics = temp[name_playlist]
    else:
      new_musics = [self.musicas.get(name_music, [])]
    new_value = {name_playlist: new_musics}
    self.raiz = self.tree.search_update(self.raiz,name_playlist,new_value)

  def play_music(self,name):
    temp = self.musicas.get(name, {})
    play(temp.get('nome_musica_usuario'))    

  def play_playlist(self,name_playlist):
    temp = self.tree.search(self.raiz,name_playlist)
    list_musics = temp.get(name_playlist,[])
    for music in list_musics:
      play(music.get('nome_musica_usuario'))

  def list_musics(self,):
    print(self.musicas)
    input("\n\nPressione Enter para continuar...")


  def list_playlist(self,):
    self.tree.pretty_print(self.raiz)
    input("\n\nPressione Enter para continuar...")
