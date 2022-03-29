from flask import Flask, render_template, request, redirect, session, flash

from flask_mysqldb import MySQL
from dao import TarefaDao

from models import Tarefa, Usuario, lista

app = Flask(__name__)
app.secret_key = 'ENGII'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'eng2'
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

# Dao

tarefa_dao = TarefaDao(db)

@app.route('/')
def index():
    return render_template('index.html', tarefas=lista)


@app.route('/novo')
def novo():
    
    return render_template('novo.html')


@app.route('/criar', methods=['POST, '])
def criar():
    nome = request.form['nome']
    descricao = request.form['descricao']
    tipo = request.form['tipo']
    status = request.form['status']
    prioridade = request.form['prioridade']
    
    tarefa = Tarefa(nome, descricao, tipo, status, prioridade)
    
    tarefa = tarefa_dao.salvar(tarefa)
    
    return redirect('/novo')


@app.route('/status')
def status():
    return render_template('status.html')


if __name__ == '__main__':

    app.run(debug=True)

        