from flask import Flask
from time import sleep
from candy import Candy

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bem vindo ao Schokotron, caralho'
@app.route('/candies')
def candies():
    c = Candy()
    print("Esta a abrir, caralho")
    c.set_duty_cycle(5.0)
    print("Esta fechar, caralho")
    c.set_duty_cycle(2.0)
    
    return 'Pintarolas, caralho!'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
