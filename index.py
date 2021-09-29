from flask import Flask,request,redirect,session,flash
from flask.templating import render_template
from flask_mysqldb import MySQL
app = Flask(__name__)
app.secret_key='alura'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticado',methods=['POST'],)
def autenticado():
    session['usuario_logado'] = request.form['usuario']
    flash("LOGADO")
    return render_template('autenticado.html')




app.run(debug=True)