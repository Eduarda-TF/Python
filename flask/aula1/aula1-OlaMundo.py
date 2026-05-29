from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route("/decorator")
def explicar_decorator():
    explicacao = """
    <h2>1. O que é um Decorator?</h2>
    <p>Um decorator é uma função especial em Python que recebe outra função como argumento, 
    estende ou modifica o seu comportamento, e retorna uma nova função, tudo isso sem alterar 
    diretamente o código-fonte da função original.</p>
    
    <h2>2. Para que serve?</h2>
    <p>Ele serve para reaproveitar código e separar responsabilidades. É ideal para implementar 
    funcionalidades transversais como controle de autenticação, logs do sistema, medição de tempo 
    de execução de blocos de código e cache de dados.</p>
    
    <h2>3. Como ele é utilizado no Flask?</h2>
    <p>No Flask, o decorator mais famoso é o <b>@app.route</b>. Ele é utilizado para associar 
    uma URL específica do navegador a uma função Python que processará a requisição. O Flask usa 
    esse decorator nos bastidores para registrar a rota no sistema de roteamento do framework, 
    garantindo que o código certo seja executado quando a página for acessada.</p>
    """
    return explicacao

@app.route('/hello') # Isso é outro decorator, mapeando a função abaixo para a rota '/hello'
def hello():
    return 'Hello, World!' # Isso é o que será retornado quando a rota '/hello' for acessada

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento
