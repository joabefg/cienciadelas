-- =====================================================
-- BANCO DE DADOS - RANKING DO JOGO
-- =====================================================

CREATE DATABASE RankingJogo;

USE RankingJogo;


-- =====================================================
-- TABELA DE PARTIDAS
-- =====================================================

CREATE TABLE Partidas (
    id INT IDENTITY(1,1) PRIMARY KEY,

    jogador1 VARCHAR(100) NOT NULL,

    jogador2 VARCHAR(100) NOT NULL,

    tempo_segundos DECIMAL(10,2) NOT NULL,

    resultado VARCHAR(20) NOT NULL,

    data_partida DATETIME DEFAULT GETDATE(),

    CONSTRAINT CK_Partidas_Tempo
        CHECK (tempo_segundos >= 0),

    CONSTRAINT CK_Partidas_Resultado
        CHECK (resultado IN ('VITORIA', 'DERROTA'))
);

-- =====================================================
-- DADOS PARA TESTE
-- =====================================================
-- Os dados de teste ainda não foram adicionados.
-- Esta tabela será conectada posteriormente ao SQLite
-- para que as partidas sejam registradas automaticamente
-- pelo jogo.
-- =====================================================

INSERT INTO Partidas
    (jogador1, jogador2, tempo_segundos, resultado)
VALUES
    ('Victor', 'Joao', 278.43, 'VITORIA'),

    ('Maria', 'Pedro', 312.50, 'VITORIA'),

    ('Lucas', 'Ana', 401.72, 'VITORIA'),

    ('Carlos', 'Julia', 450.18, 'DERROTA'),

    ('Rafael', 'Bruno', 289.90, 'VITORIA');


-- =====================================================
-- CONSULTA DO RANKING
-- =====================================================

SELECT
    ROW_NUMBER() OVER (
        ORDER BY tempo_segundos ASC
    ) AS posicao,

    jogador1,
    jogador2,

    tempo_segundos,

    resultado,

    data_partida

FROM Partidas

WHERE resultado = 'VITORIA'

ORDER BY tempo_segundos ASC;

-- TODO: Conectar ao SQLite e implementar a inserção
-- automática dos dados das partidas.