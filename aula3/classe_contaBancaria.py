''' 
    Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo.
    Inicie o atributo ativo como False por padrão.

    Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos.
    Utilize propriedades, se necessário.
'''
class ContaBancaria:
    def __init__(self, titular='', saldo=0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
    '''
    Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta.
    Crie duas instâncias da classe e imprima essas instâncias.
    '''
    def __str__(self) -> str:
        return f' titular: {self._titular.ljust(10)} | Saldo: R${self._saldo}'
    '''
        Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True.
        Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    '''
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
        
    @property
    def ativo(self):
        return 'Ativado' if self.ativo else 'Desativado'

'''
    Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos.
    Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
'''
class ClienteBanco:
    def __init__(self, nome, sobrenome, idade, endereco, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade
        self._endereco = endereco
        self._cpf = cpf
    '''
        Crie um método de classe para a conta ClienteBanco.
    '''
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta

pessoa1 = ClienteBanco('Alice', 'Gonçalves', 27, 'Rua das flores, n140', '123.456.787-79')
pessoa2 = ClienteBanco('Rafael', 'Constâncio', 41, 'Rua das magnolias, n90', '123.456.007-70')
pessoa3 = ClienteBanco('Gustavo', 'Benedito', 37, 'Rua das arvores, n50', '123.456.111-71')

conta1 = ContaBancaria('Gabriel', 800)
conta2 = ContaBancaria('Gabriela', 3800)
conta3 = ContaBancaria("Carlos", 200)

print(conta1)
print(conta2)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")

conta_cliente1 = ClienteBanco.criar_conta('Rafaela', 1500)
print(f'Conta de {conta_cliente1._titular} foi criada com saldo de R${conta_cliente1._saldo}')