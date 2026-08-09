-- ============================================
-- ENTIDADE: Modelo
-- Responsável (Banco): Joab
-- Responsável (Back): Joab
-- Última atualização: 09/08/2026
-- ============================================

USE cienciadelas;

-- ============================================
-- 1. DDL - CRIAÇÃO DA TABELA
-- ============================================

CREATE TABLE IF NOT EXISTS modelo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    atributo VARCHAR(255) NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- 2. DML - CRUD
-- ============================================

-- 2.1 CREATE: criar um novo registro
-- Parâmetro: valor:String
INSERT INTO modelo (atributo) VALUES (valor);

-- 2.2 RFAD: listar todos os registros
SELECT * FROM modelo;

-- buscar um registro por ID
-- Parâmetro: id_valor:int
SELECT * FROM modelo WHERE id = id_valor;

-- 2.3 UPDATE: atualizar um registro existente
-- Parâmetros: valor:String, id_valor:int
UPDATE modelo SET atributo = valor WHERE id = id_valor;

-- 2.4 DELETE: deletar um registro
-- Parâmetro: id_valor:int
DELETE FROM modelo WHERE id = id_valor;

-- ============================================
-- 3. DML - CONSULTAS EXTRAS
-- ============================================

-- 3.1 Contar quantos registros existem (paginação)
SELECT COUNT(*) AS total FROM modelo;


-- 3.2 Listar os 5 registros mais recentes
SELECT * FROM modelo ORDER BY criado_em DESC LIMIT 5;

-- ============================================
-- 4. POPULAR BANCO VIA API
-- ============================================

INSERT INTO modelo (atributo) VALUES
    ('Registro de teste 1'),
    ('Registro de teste 2'),
    ('Registro de teste 3');