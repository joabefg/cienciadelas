import pytest
from unittest.mock import patch
from app import app


@pytest.fixture
def cliente():
    app.config["TESTING"] = True

    with app.test_client() as cliente:
        yield cliente


def test_listar_faq(cliente):
    with patch(
        "faq_route.faq_controller.listar_perguntas",
        return_value=[]
    ):
        resposta = cliente.get("/api/faq")

    assert resposta.status_code == 200
    assert resposta.json == []


def test_criar_faq(cliente):
    with patch(
        "faq_route.faq_controller.cadastrar_pergunta",
        return_value={
            "id": 1,
            "pergunta": "O que é Ciência Delas?",
            "resposta": "Um projeto de divulgação científica."
        }
    ):
        resposta = cliente.post(
            "/api/faq",
            json={
                "pergunta": "O que é Ciência Delas?",
                "resposta": "Um projeto de divulgação científica."
            }
        )

    assert resposta.status_code == 201


def test_criar_faq_sem_dados(cliente):
    resposta = cliente.post("/api/faq", json={})

    assert resposta.status_code == 400