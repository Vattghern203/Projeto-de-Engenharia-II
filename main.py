from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'ENGII'

class Tarefa:
    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria

tarefa01 = Tarefa('Estudar', 'Estudos')
tarefa02 = Tarefa('Compras', 'Dia-a-dia')
tarefa03 = Tarefa('Jogar LOL', 'Alta importância')

lista = [tarefa01, tarefa02, tarefa03]

@app.route('/')
def index():
    return render_template('index.html', tarefas=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html')

@app.route('/status')
def status():
    return render_template('status.html')


if __name__ == '__main__':

    app.run(debug=True)

        