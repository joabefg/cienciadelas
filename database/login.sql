USE cienciadelas;

-- ============================================
-- 1. DDL - CRIAÇÃO DA TABELA
-- ============================================

CREATE TABLE IF NOT EXISTS login (
    id_login INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    id_cad INT NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (email) REFERENCES cadastro(email),
    FOREIGN KEY (senha) REFERENCES cadastro(senha),
    FOREIGN KEY (id_cad) REFERENCES cadastro(id_cad)
);

-- ============================================
-- 2. DML - CRUD
-- ============================================

-- 2.1 CREATE: criar um novo registro
-- Parâmetro: valor:String
INSERT INTO login (email) VALUES ("juquinhagames@email.com");

-- 2.2 RFAD: listar todos os registros
SELECT * FROM login;

-- buscar um registro por ID
-- Parâmetro: id_valor:int
SELECT * FROM login WHERE id_login = 1;

-- 2.3 UPDATE: atualizar um registro existente
-- Parâmetros: valor:String, id_valor:int
UPDATE login SET senha = '12345678' WHERE id_login = 1;

-- 2.4 DELETE: deletar um registro
-- Parâmetro: id_valor:int
DELETE FROM login WHERE id_login = 1;

-- ============================================
-- 3. DML - CONSULTAS EXTRAS
-- ============================================

-- 3.1 Contar quantos registros existem (paginação)
SELECT COUNT(*) AS total FROM login;


-- 3.2 Listar os 5 registros mais recentes
SELECT * FROM login ORDER BY criado_em DESC LIMIT 5;

-- ============================================
-- 4. POPULAR BANCO VIA API
-- ============================================

INSERT INTO login (email, senha) VALUES
    ('ciencia.delas@gmail.com', '12345678'),
    ('juquinhas@gmail.com', '12345'),
    ('teste123@gmail.com', 'teste123');