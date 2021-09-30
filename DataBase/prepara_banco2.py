import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='', host='localhost', port=3306)


criando_tabela='''
    USE `USUARIOS`;
   CREATE TABLE ENTRADA(
       IDENTRADA INT PRIMARY KEY AUTO_INCREMENT,
        DINHEIRO INT(6),
        LOCAL VARCHAR(100),
        DATA DATE,
        ID_LOGIN INT
   ) ;

'''

conn.cursor().execute(criando_tabela)
cursor = conn.cursor()

cursor.close()