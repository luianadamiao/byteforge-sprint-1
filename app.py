from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Olá, mundo! Flask está funcionando!'

@app.route('/ping/<nome>')
def ping(nome):
    
    print(f"O nome recebido foi: {nome}")
    return f"Pong! Você passou o nome: {nome}"

if __name__ == '__main__':
    app.run(debug=True)