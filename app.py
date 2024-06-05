#importar 
from flask import Flask

#crear una app 
app = Flask(__name__)

@app.route('/')
def home():
    return "Hola mundo"


#mandamos a llamar al objetos y lo corremos con run 
if __name__ == '__main__': 
    app.run(debug=True)