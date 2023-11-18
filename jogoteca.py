from flask import Flask, render_template, request, redirect
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'puzzle', 'atari')
jogo2 = Jogo('csGo', 'Tiro', 'pc')
jogo3 = Jogo('Read dead Redenption', 'Ação', 'Todos')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo= 'jogos', jogos =lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo = 'novo jogo')
@app.route('/criar', methods = ['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

app.run(debug=True)