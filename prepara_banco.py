import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='', host='localhost', port=3306)
# Descomente se quiser desfazer o banco...
#conn.cursor().execute("DROP DATABASE `jogoteca`;")
#conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `usuario` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `usuario`;
    CREATE TABLE `login` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) COLLATE utf8_bin NOT NULL,
      `senha` varchar(40) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    '''

conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO usuario.login (id, nome, senha) VALUES (%s, %s, %s)',
      [
            ('1', 'Erick', 'Erick'),
            ('2', 'Bruno', 'Erick'),
            ('3', 'Iris', 'Erick')
      ])

cursor.execute('select * from usuario.login')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
#cursor.executemany(
 #     'INSERT INTO jogoteca.jogo (nome, categoria, console) VALUES (%s, %s, %s)',
  #    [
   #         ('God of War 4', 'Ação', 'PS4'),
    #        ('NBA 2k18', 'Esporte', 'Xbox One'),
     #       ('Rayman Legends', 'Indie', 'PS4'),
      #      ('Super Mario RPG', 'RPG', 'SNES'),
       #     ('Super Mario Kart', 'Corrida', 'SNES'),
        #    ('Fire Emblem Echoes', 'Estratégia', '3DS'),
      #])

cursor.execute('select * from usuario.login')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()