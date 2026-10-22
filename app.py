from flask import Flask, render_template

# Instancia a API
app = Flask(__name__)

# Cria a rota /evento
@app.route("/")
def cadastrar_eventos():
    return render_template("home.html")

# Sobe o servidor
if __name__ == "__main__":
    app.run(debug=True)