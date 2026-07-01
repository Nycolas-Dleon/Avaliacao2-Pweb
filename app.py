from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'pneumoultramicroscopicosilicovulcanoniotico'

# --- Funções Auxiliares e session ---

def obter_filmes():
    # Retorna a lista de filmes ou uma lista vazia se não existir
    return session.get('filmes', [])

def adicionar_filme(titulo):
    filmes = obter_filmes()
    filmes.append(titulo)
    session['filmes'] = filmes
    session.modified = True

def remover_filme(indice):
    filmes = obter_filmes()
    if 0 <= indice < len(filmes):
        filmes.pop(indice)
        session['filmes'] = filmes
        session.modified = True

def contar_filmes():
    return len(obter_filmes())

# --- Rotas ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        if titulo:
            adicionar_filme(titulo)
            return redirect(url_for('sucesso'))
    
    filmes = obter_filmes()
    total = contar_filmes()
    return render_template('index.html', filmes=filmes, total=total)

@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

@app.route('/remover/<int:indice>')
def remover(indice):
    remover_filme(indice)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)