from repositorios import faq_model


def listar_perguntas():
    return faq_model.listar_todos()


def cadastrar_pergunta(pergunta, resposta):
    if not pergunta or not resposta:
        return None

    return faq_model.criar(pergunta, resposta)