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

if __name__ == '__main__':
    app.run(debug=True)