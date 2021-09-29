from flask import Flask,request,redirect,session,flash
from flask.templating import render_template
from flask_mysqldb import MySQL
from dao import DBusuario
from models import Cadastro


app = Flask(__name__)
app.secret_key='alura'
app.config['MYSQL_HOST'] = "0.0.0.0"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "usuario"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

usuario_dao=DBusuario(db)


@app.route('/')
def index():
    lista = usuario_dao.listar()
    return render_template('index.html',usuarios = lista)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup',)
def signup():
    nome = request.form['usuario']
    senha = request.form['senha']
    novo_usuario=Cadastro(nome,senha)
    usuario_dao.salvar(novo_usuario)
    return render_template('/signup')


@app.route('/autenticado',methods=['POST'],)
def autenticado():
    session['usuario_logado'] = request.form['usuario']
    flash("LOGADO")
    return render_template('autenticado.html')




app.run(debug=True)