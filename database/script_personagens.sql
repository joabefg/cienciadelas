USE cienciadelas;

-- Criação da tabela 'personagem' 
CREATE TABLE IF NOT EXISTS personagem (
    id_personagem INT AUTO_INCREMENT PRIMARY KEY,
    nome_personagem VARCHAR(50) NOT NULL,
    descricao_personagem VARCHAR(255),
    biografia_personagem VARCHAR(300),
    ano_nascimento INT,
    ano_falecimento INT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inserção de um registro de exemplo (equivalente ao POST /personagens)
INSERT INTO personagem (nome_personagem, descricao_personagem, biografia_personagem, ano_nascimento, ano_falecimento) 
VALUES ('Nome Exemplo', 'Descrição breve do personagem', 'Biografia detalhada do personagem científico.', 1900, 1980);

-- Consulta de todos os registros (equivalente ao GET /personagens)
SELECT * FROM personagem;

-- Consulta de um registro específico por ID (equivalente ao GET /personagens/{id})
SELECT * FROM personagem WHERE id_personagem = 1;

-- Atualização de um registro por ID
UPDATE personagem 
SET nome_personagem = 'Nome Atualizado', 
    descricao_personagem = 'Nova descrição atualizada' 
WHERE id_personagem = 1;

-- Exclusão de um registro por ID
DELETE FROM personagem WHERE id_personagem = 1;

-- Contagem total de registros
SELECT COUNT(*) AS total FROM personagem;

-- Consulta dos últimos registros adicionados
SELECT * FROM personagem ORDER BY criado_em DESC LIMIT 5;

-- Inserção de múltiplos registros de teste (cientistas célebres)
INSERT INTO personagem (nome_personagem, descricao_personagem, biografia_personagem, ano_nascimento, ano_falecimento) VALUES
    ('Marie Curie', 'Física e química pioneira na radioatividade', 'Marie Curie conduziu pesquisas pioneiras e foi a primeira mulher a ganhar um Prêmio Nobel.', 1867, 1934);

