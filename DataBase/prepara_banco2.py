import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='', host='localhost', port=3306)


criando_tabela_entrada='''
    USE `USUARIOS`;
   CREATE TABLE ENTRADA(
       IDENTRADA INT PRIMARY KEY AUTO_INCREMENT,
        DINHEIRO INT(6),
        LOCAL VARCHAR(100),
        DATA DATE,
        ID_LOGIN INT
   ) ;

'''

criando_tabela_saida='''
    USE `USUARIOS`;
   CREATE TABLE SAIDA(
       IDSAIDA INT PRIMARY KEY AUTO_INCREMENT,
        DINHEIRO INT(6),
        LOCAL VARCHAR(100),
        DATA DATE,
        ID_LOGIN INT
   ) ;

'''

conn.cursor().execute(criando_tabela_entrada)

cursor = conn.cursor()
conn.cursor().execute(criando_tabela_saida)
cursor = conn.cursor()

cursor.close()