from flask import Flask, render_template, request
class jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


app = Flask(__name__)

@app.route('/inicio')
def ola():

    jogo1 = jogo('Tetris', 'puzzle', 'atari')
    jogo2 = jogo('csGo', 'Tiro', 'pc')
    jogo3 = jogo('Read dead Redenption', 'Ação', 'Todos')


    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo= 'jogos', jogos =lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo = 'novo jogo')

app.run()