from models import Cadastro,Entrada_de_Dinheiro

SQL_DELETA_USUARIO = 'delete from login where email = %s'
SQL_USUARIO_POR_ID = 'Select email,senha from login where email=%s'
SQL_ATUALIZA_USUARIO = 'UPDATE login SET email=%s, senha=%s where email=%s'
SQL_CRIA_USUARIO = 'INSERT INTO login(email,senha) values(%s,%s)'
SQL_BUSCA_USUARIOS = 'SELECT id, email,senha from login'


SQL_ADICIONA_ENTRADA='INSERT INTO ENTRADA(DINHEIRO,LOCAL,DATA,ID_LOGIN) VALUES(%s,%s,%s,%s)'
SQL_BUSCA_ENTRADA = 'SELECT IDENTRADA,DINHEIRO,LOCAL,DATA,ID_LOGIN FROM ENTRADA'

SQL_ADICIONA_SAIDA='INSERT INTO SAIDA(DINHEIRO,LOCAL,DATA,ID_LOGIN) VALUES(%s,%s,%s,%s)'

class DBusuario:
    def __init__(self,db):
        self.__db=db

    def salvar(self,user):
        cursor = self.__db.connection.cursor()

        
        # faz ele
        cursor.execute(SQL_CRIA_USUARIO,(user.email,user.senha))
        user.id=cursor.lastrowid
        self.__db.connection.commit()
        return user

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_USUARIOS)
        usuarios = traduz_nome(cursor.fetchall())
        return usuarios

    def busca_por_id(self,email):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID,(email,))
        dados = cursor.fetchone()
        usuario=traduz_usuario(dados) if dados else None
        return usuario

class Entrada_Saida_Dinheiro():
    def __init__(self,db):
        self.__db=db

    def criandoEntrada(self,dinheiro):
        cursor = self.__db.connection.cursor()

        cursor.execute(SQL_ADICIONA_ENTRADA,(dinheiro.dinheiro,dinheiro.local,dinheiro.data,dinheiro.id_login))
        dinheiro.id=cursor.lastrowid
        self.__db.connection.commit()
        return dinheiro

    def criandoSaida(self,dinheiro):
        cursor = self.__db.connection.cursor()

        cursor.execute(SQL_ADICIONA_SAIDA,(dinheiro.dinheiro,dinheiro.local,dinheiro.data,dinheiro.id_login))
        dinheiro.id=cursor.lastrowid
        self.__db.connection.commit()
        return dinheiro

    def listar_Entrada(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_ENTRADA)
        usuarios = traduz_dinheiro(cursor.fetchall())
        return usuarios

def traduz_nome(nome):
    def cria_nome_com_tupla(tupla):
        return Cadastro(tupla[1], tupla[2], id=tupla[0])
    return list(map(cria_nome_com_tupla, nome))

def traduz_dinheiro(dinheiro):
    def cria_nome_com_tupla(tupla):
        return Entrada_de_Dinheiro(tupla[1], tupla[2],tupla[3],tupla[4], id=tupla[0])
    return list(map(cria_nome_com_tupla, dinheiro))

def traduz_usuario(tupla):
    return Cadastro(tupla[0], tupla[1])