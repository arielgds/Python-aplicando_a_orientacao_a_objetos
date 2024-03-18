

class Musica:
    nome: ' ' # type: ignore
    artista: ' ' # type: ignore
    duracao: int

musica1 = Musica()
musica1.nome = 'Plush'
musica1.artista = 'Stone Temple Pilots'
musica1.duracao = 310

print(vars(musica1))

musica2 = Musica()
musica2.nome = 'Its Not Unusual '
musica2.artista = 'Tom Jones'
musica2.duracao = 120
print(vars(musica2))

musica3 = Musica()
musica3.nome = 'Everybody Wants To Rule The World'
musica3.artista = 'Tears For Fears'
musica3.duracao = 251
print(vars(musica3))
