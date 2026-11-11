from flask import Flask
from flask_cors import CORS
import os

from modelo_route import modelo_bp
from faq_route import faq_bp
from repositorios.faq_model import criar_tabela

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "frontend", "static"),
    static_url_path="/static"
)

CORS(app)

app.register_blueprint(modelo_bp)
app.register_blueprint(faq_bp)

criar_tabela()


if __name__ == "__main__":
    app.run(debug=True)