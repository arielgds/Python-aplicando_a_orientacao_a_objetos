'''
    -Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão.
    -Adicione um método especial __str__ para imprimir uma representação em string da pessoa.
    -Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano.
    -Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.
'''

class Pessoa:
    def __init__(self, nome='', idade=int, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profisssao = profissao
    
    def __str__(self):
        return f'{self.nome} |  {self.idade} | {self.profisssao}'
    
    def aniversario(self):
        self.idade += 1

    def saudacao(self):
        if self.profisssao:
            return f'Olá, sou {self.nome}, tenho {self.idade} anos e minha profissão é {self.profisssao}'
        else:
            return f'Olá, meu nome é {self.nome}!'
        
pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

print(pessoa1)
print(pessoa2)
print(pessoa3)
print()