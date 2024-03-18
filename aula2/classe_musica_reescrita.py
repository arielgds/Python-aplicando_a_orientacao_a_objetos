'''
    Reescrevendo a Classe da aula1, de uma forma mais concisa com a sintaxe do python
'''


class Musica:
    def __init__(self, nome='', artista='', duracao=0):
        self.nome: nome
        self.artista: artista
        self.duracao: duracao

musica1 = Musica(nome='Plush', artista='Stone Temple Pilots', duracao= 310)

musica2 = Musica(nome='Its Not Unusual', artista='Tom Jones', duracao= 120)

musica3 = Musica(nome='Everybody Wants To Rule The World', artista='Tears For Fears', duracao= 251)
