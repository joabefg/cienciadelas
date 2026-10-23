from flask import Flask, render_template, request
from flask_cors import CORS
from controllers.modelo_controller import listar_modelo, salvar_modelo

app = Flask(__name__)
CORS(app)

@app.route("/")
def home_route():
    return render_template("home.html")

@app.route("/modelo", methods=["GET", "POST"])
def modelo_route():

    if request.method == "POST":
        salvar_modelo()

    lista = listar_modelo()
    return render_template("modelo.html", lista = lista)

if __name__ == "__main__":
    app.run(debug=True)