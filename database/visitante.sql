CREATE DATABASE IF NOT EXISTS cienciadelas
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
  -- ============================================
-- ENTIDADE: Visitante
-- Responsável (Banco): Esther
-- Responsável (Back): Esther
-- Última atualização: 10/08/2026
-- ============================================


USE cienciadelas;


-- ============================================
-- 1. DDL - CRIAÇÃO DA TABELA
-- ============================================

CREATE TABLE IF NOT EXISTS cadastro (
    id_cad INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- ============================================
-- 2. DML - CRUD
-- ============================================


-- 2.1 CREATE: criar um novo visitante
-- Parâmetros: email:String, senha:String
INSERT INTO cadastro (email, senha)
VALUES ("joinha@gmail.com", 321456);


-- 2.2 READ: listar todos os visitantes
SELECT * FROM cadastro;


-- Buscar um visitante por ID
-- Parâmetro: id_valor:int
SELECT * FROM cadastro
WHERE id_cad = 1;


-- Buscar um visitante por email
-- Parâmetro: email_valor:String
SELECT * FROM cadastro
WHERE email = "estherlegal@gmail.com";


-- 2.3 UPDATE: atualizar um visitante existente
-- Parâmetros: email:String, senha:String, id_valor:int
UPDATE cadastro
SET email = "estherlegal@gmail.com",
    senha = "12345678"
WHERE id_cad = 1;


-- Atualizar somente a senha
-- Parâmetros: senha:String, id_valor:int
UPDATE cadastro
SET senha = "12345678"
WHERE id_cad = 1;


-- 2.4 DELETE: deletar um visitante
-- Parâmetro: id_valor:int
DELETE FROM cadastro
WHERE id_cad = 1;
                        

-- ============================================
-- 3. DML - CONSULTAS EXTRAS
-- ============================================


-- 3.1 Contar quantos visitantes existem
SELECT COUNT(*) AS total
FROM cadastro;


-- 3.2 Listar os 5 visitantes mais recentes
SELECT *
FROM cadastro
ORDER BY criado_em DESC
LIMIT 5;


-- ============================================
-- 4. POPULAR BANCO VIA API
-- ============================================

INSERT INTO cadastro (email, senha) VALUES
    ('visitante1@email.com', 'senha123'),
    ('visitante2@email.com', 'senha456'),
    ('visitante3@email.com', 'senha789');