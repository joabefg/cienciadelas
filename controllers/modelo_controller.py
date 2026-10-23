from models.modelo import Modelo
from flask import request, render_template_string

def salvar_modelo():
    atributo = request.form["atributo"]
    criacao = request.form["criacao"]
    modelo = Modelo(atributo, criacao)
    registros =  modelo.salvar()
    return registros

def listar_modelo():
    return Modelo.listar()
