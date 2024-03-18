'''
    Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao.
    Inicie um atributo chamado disponivel como True por padrão.
'''

class Livro:
    def __init__(self, titulo, autor, ano_publicacao) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
    '''
        Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro.
        Crie duas instâncias da classe Livro e imprima essas instâncias.
    '''
    def __str__(self):
        return f'Título: {self.titulo} | Autor: {self.autor} | Ano de publicação: {self.ano_publicacao}'
    '''
        Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False.
        Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    '''
    def emprestar(cls, livro):
        livro.disponivel = False
    '''
        Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    '''
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis
    
livro1 = Livro('O Segredo', 'Rhonda Byrne', 2005)
livro2 = Livro('A Arte da Sedução', 'Robert Greene', 2013)
livro3 = Livro("Aprendendo Python", "John Doe", 2022)

Livro.livros = [livro1,livro2,livro3]
    
