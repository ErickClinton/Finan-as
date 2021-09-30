from models import Cadastro

SQL_DELETA_USUARIO = 'delete from login where email = %s'
SQL_USUARIO_POR_email = 'Select id,email,senha from login where email=%s'
SQL_ATUALIZA_USUARIO = 'UPDATE login SET email=%s, senha=%s where email=%s'
SQL_CRIA_USUARIO = 'INSERT INTO login(email,senha) values(%s,%s)'
SQL_BUSCA_USUARIOS = 'SELECT id, email,senha from login'


SQL_ADICIONA_ENTRADA='INSERT INTO ENTRADA(DINHEIRO,LOCAL,DATA,ID_LOGIN) VALUES(%s,%s,%s,%s)'
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
        jogos = traduz_nome(cursor.fetchall())
        return jogos

    def busca_por_email(self,email):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_email,(email,))
        dados = cursor.fetchone()
        usuario=traduz_nome(dados) if dados else None
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



def traduz_nome(nome):
    def cria_nome_com_tupla(tupla):
        return Cadastro(tupla[1], tupla[2], id=tupla[0])
    return list(map(cria_nome_com_tupla, nome))
