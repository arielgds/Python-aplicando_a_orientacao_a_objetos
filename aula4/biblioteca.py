'''
    Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
'''
from livros import Livro

livro1 = Livro('O Segredo', 'Rhonda Byrne', 2005)
livro2 = Livro('A Arte da Sedução', 'Robert Greene', 2014)
'''
    No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
'''
Livro.emprestar(livro2)
Livro.verificar_disponibilidade(livro2)
'''
    No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
'''
ano_especifico = 2014
livros_disp_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f'Livros disponíveis em {ano_especifico}: {livros_disp_ano}')