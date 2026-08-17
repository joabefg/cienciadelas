from flask import Flask
from flask_cors import CORS
from modelo_route import modelo_bp
from personagens_route import personagens_bp 
from cartas_route import cartas_bp


app = Flask(__name__)
CORS(app)

# Pessoal, registra seu próprio blueprint aqui e não esquece de importar a entidade_bp
app.register_blueprint(modelo_bp)
app.register_blueprint(personagens_bp)
app.register_blueprint(cartas_bp)

if __name__ == "__main__":
    app.run(debug=True)