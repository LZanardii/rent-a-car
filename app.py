from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

from routes import *

if __name__ == '__main__':
    app.run(debug=True)

#TODO bugfix-renderizar somente clientes com locação em aberto
#TODO bugfix-atualizar cidade_origem do veiculo após a devolução
