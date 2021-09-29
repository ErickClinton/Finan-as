from models import Cadastro

SQL_DELETA_USUARIO = 'delete from login where id = %s'
SQL_USUARIO_POR_ID = 'Select id,nome,senha from login where id=%s'
SQL_ATUALIZA_USUARIO = 'UPDATE login SET nome=%s, senha=%s where id=%s'
SQL_CRIA_USUARIO = 'INSERT INTO login(id,nome,senha) values(%s,%s,%s)'
SQL_BUSCA_USUARIOS = 'SELECT id, nome,senha from login'
class DBusuario:
    def __init__(self,db):
        self.__db=db

    def salvar(self,nome):
        cursor = self.__db.connection.cursor()

        if(nome.id):
            cursor.execute(SQL_ATUALIZA_USUARIO,(nome.id,nome.nome,nome.senha))
        else:
            cursor.execute(SQL_CRIA_USUARIO,(nome.id, nome.nome,nome.senha))
            nome.id=cursor.lastrowid
        self.__db.connection.commit()
        return nome

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_USUARIOS)
        jogos = traduz_nome(cursor.fetchall())
        return jogos

def traduz_nome(nome):
    def cria_nome_com_tupla(tupla):
        return Cadastro(tupla[1], tupla[2], id=tupla[0])
    return list(map(cria_nome_com_tupla, nome))
