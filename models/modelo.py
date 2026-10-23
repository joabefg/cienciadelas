from config import conectar

class Modelo:
    def __init__(self, atributo, criado_em):
        self.atributo = atributo
        self.criado_em = criado_em
    
    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """
        INSERT INTO modelo (atributo, criado_em)
        VALUES (%s, %s)
        """
        valores = (self.atributo, self.criado_em)
        cursor.execute(sql, valores)
        reg_salvos = cursor.rowcount
        conexao.commit()
        cursor.close()
        conexao.close()
        return reg_salvos

    def listar():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM modelo")
        lista = cursor.fetchall()
        cursor.close()
        conexao.close()
        return lista