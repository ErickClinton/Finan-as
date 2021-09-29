from flask import Flask,request,redirect,session,flash
from flask.helpers import url_for
from flask.templating import render_template
from flask_mysqldb import MySQL
from dao import DBusuario
from models import Cadastro


app = Flask(__name__)
app.secret_key='alura'

#conexao com o banco de dados
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "usuario"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

usuario_dao=DBusuario(db)

#rota principal
@app.route('/')
def index():
    return render_template("template.html")

    #'lista.html',titulo="usuarios",usuarios = lista



#Rota para o login
@app.route('/novo')
def login():
    return render_template('login.html')

#cadastro ainda nao funcionando
@app.route('/signup', methods=['POST',])
def signup():
    nome = request.form['usuario']
    senha = request.form['senha']
    novo_usuario=Cadastro(nome,senha)
    usuario_dao.salvar(novo_usuario)
    return redirect(url_for('lista'))


#apenas teste
@app.route('/autenticado',methods=['POST'],)
def autenticado():
    session['usuario_logado'] = request.form['usuario']
    flash("LOGADO")
    return render_template('autenticado.html')


@app.route('/lista')
def lista():
    lista = usuario_dao.listar()
    return render_template('lista.html',titulo="usuarios",usuarios = lista)


app.run(debug=True)