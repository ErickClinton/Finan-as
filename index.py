from flask import Flask,request,redirect,session,flash
from flask.helpers import url_for
from flask.templating import render_template
from flask_mysqldb import MySQL
from dao import DBusuario, Entrada_Saida_Dinheiro
from models import Cadastro, Entrada_de_Dinheiro


app = Flask(__name__)
app.secret_key='alura'

#conexao com o banco de dados
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "USUARIOS"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

usuario_dao=DBusuario(db)
dinheiro_dao = Entrada_Saida_Dinheiro(db)
#rota principal
@app.route('/')
def index():
    return render_template("template.html")

    #'lista.html',titulo="usuarios",usuarios = lista



#Rota para o o cadastro
@app.route('/novo')
def cadastro():
    return render_template('cadastro.html')

#cadastro FUNCIONANDO
@app.route('/signup', methods=['POST',])
def signup():
    nome = request.form['usuario']
    senha = request.form['senha']
    novo_usuario=Cadastro(nome,senha)
    usuario_dao.salvar(novo_usuario)
    return redirect(url_for('lista'))



@app.route('/login')
def login():
    return render_template('login.html')




#apenas teste
@app.route('/autenticado',methods=['POST'],)
def autenticado():
    usuario = usuario_dao.busca_por_id(request.form['email'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(url_for('lista'))
    else:
        flash('Não logado, tente denovo!')
        return redirect(url_for('login'))

    flash("LOGADO")
    return render_template('autenticado.html')


@app.route('/lista')
def lista():
    lista = usuario_dao.listar()
    return render_template('lista.html',titulo="usuarios",usuarios = lista)

#APARTIR DAQUI É SOBRE ENTRADA E SAIDA DE DINHEIRO

@app.route('/novoDinheiro')
def novoDinheiro():
    return render_template('entrada.html')



@app.route('/entrada', methods=['POST',])
def entradadinheiro():
    dinheiro = request.form['dinheiro']
    local = request.form['local']
    data = request.form['data']
    id_login = request.form['id_login']
    Dinheiro_Entrando = Entrada_de_Dinheiro(dinheiro,local,data,id_login)
    dinheiro_dao.criandoEntrada(Dinheiro_Entrando)
    return redirect(url_for('lista'))

app.run(debug=True)