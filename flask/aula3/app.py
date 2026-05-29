from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    nome = "Eduarda"
    idade = 22
    nota = 8.5
    usuario = {"nome": "Eduarda", "email": "eduarda@email.com"}
    alunos = ["Carlos", "Mariana", "João", "Beatriz"]

    return render_template(
        "index.html",
        nome=nome,
        idade=idade,
        usuario=usuario,
        alunos=alunos,
        nota=nota,
    )


if __name__ == "__main__":
    app.run(debug=True)