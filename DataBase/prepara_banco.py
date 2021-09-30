import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='', host='localhost', port=3306)
# Descomente se quiser desfazer o banco...
#conn.cursor().execute("DROP DATABASE `jogoteca`;")
#conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `USUARIOS` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `USUARIOS`;
    CREATE TABLE `login` (
      `id` int PRIMARY KEY AUTO_INCREMENT,
      `email` varchar(50)  NOT NULL,
      `senha` varchar(40) NOT NULL
    ) ;
    '''

conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO USUARIOS.login (email, senha) VALUES (%s, %s)',
      [
            ('Erick', 'Erick'),
            ('Bruno', 'Erick'),
            ('Iris', 'Erick')
      ])

cursor.execute('select * from USUARIOS.login')
print(' -------------  USUARIOS:  -------------')
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

cursor.execute('select * from USUARIOS.login')
print(' -------------  usuarios:  -------------')
for usuarios in cursor.fetchall():
    print(usuarios[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()


