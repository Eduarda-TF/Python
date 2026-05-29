from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')


usuarios = [
    {"usuario": "marcos", "senha": "cotemig2026"},
    {"usuario": "janaina", "senha": "cotemig2026"},
    {"usuario": "eduarda", "senha": "12500364"}
]

@app.route('/login', methods=['GET', 'POST'])
def login():

    mensagem = ""

    if request.method == 'POST':

        usuario_digitado = request.form.get('usuario')
        senha_digitada = request.form.get('senha')

        acesso_liberado = False

        for usuario in usuarios:

            if usuario_digitado == usuario["usuario"] and senha_digitada == usuario["senha"]:
                acesso_liberado = True
                mensagem = f"Bem-vindo(a), {usuario_digitado}!"

        if not acesso_liberado:
            mensagem = "Login inválido!"

    return render_template('login.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)