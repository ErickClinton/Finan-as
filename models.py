#mesmo nome das tabelas no banco de dados

class Cadastro:
    def __init__(self,email, senha,id=None):
        self.id = id
        self.email = email
        self.senha = senha

class Entrada_de_Dinheiro:
    def __init__(self,dinheiro,local,data,id_login,id=None):
        self.dinheiro = dinheiro
        self.local = local
        self.data = data
        self.id_login = id_login

class Saida_de_Dinheiro:
    def __init__(self,dinheiro,local,data,id_login):
        self.dinheiro = dinheiro
        self.local = local
        self.data = data
        self.id_login = id_login