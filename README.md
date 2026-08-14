Claro. Vou deixar **tudo em um único `README.md`** e remover a parte de **estrutura planejada**.

````markdown
# 🎮 Sistema de Ranking — Banco de Dados

Banco de dados responsável pelo armazenamento das partidas e informações necessárias para o sistema de ranking do jogo.

---

## 📌 Sobre o projeto

Este banco será utilizado para armazenar os resultados das partidas realizadas no jogo, permitindo futuramente a criação de um ranking online.

A ideia é que, ao finalizar uma partida, o jogo envie as informações para uma API, que será responsável por registrar os dados no banco de dados.

### Fluxo planejado

```text
┌──────────────┐
│    Unity     │
│     Jogo     │
└──────┬───────┘
       │
       │ Resultado da partida
       ▼
┌──────────────┐
│     API      │
│   Backend    │
└──────┬───────┘
       │
       │ INSERT
       ▼
┌──────────────┐
│    SQLite    │
│   Ranking    │
└──────┬───────┘
       │
       │ SELECT
       ▼
┌──────────────┐
│     Site     │
│   Ranking    │
└──────────────┘
````

---

## 🗄️ Banco de dados

O projeto utilizará **SQLite** inicialmente.

A estrutura foi pensada para armazenar cada partida realizada no jogo.

### Tabela `partidas`

| Campo            | Tipo     | Descrição                          |
| ---------------- | -------- | ---------------------------------- |
| `id`             | INTEGER  | Identificador único da partida     |
| `jogador1`       | TEXT     | Nome do jogador 1                  |
| `jogador2`       | TEXT     | Nome do jogador 2                  |
| `tempo_segundos` | REAL     | Tempo total da partida em segundos |
| `resultado`      | TEXT     | Resultado da partida               |
| `data_partida`   | DATETIME | Data e hora da partida             |

---

## 🏆 Ranking

O ranking será baseado no **menor tempo de conclusão da partida**.

Exemplo:

```text
1º — Victor + João — 278.43 segundos
2º — Maria + Pedro — 312.50 segundos
3º — Lucas + Ana — 401.72 segundos
```

Somente partidas com resultado `VITORIA` serão consideradas no ranking.

---

## 🧱 Estrutura SQL

A tabela principal será criada através do arquivo:

```text
ranking.sql
```

Exemplo:

```sql
CREATE TABLE IF NOT EXISTS partidas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    jogador1 TEXT NOT NULL,

    jogador2 TEXT NOT NULL,

    tempo_segundos REAL NOT NULL,

    resultado TEXT NOT NULL,

    data_partida DATETIME DEFAULT CURRENT_TIMESTAMP,

    CHECK (tempo_segundos >= 0),

    CHECK (resultado IN ('VITORIA', 'DERROTA'))
);
```

---

## 🔎 Consulta do ranking

Para obter o ranking:

```sql
SELECT
    ROW_NUMBER() OVER (
        ORDER BY tempo_segundos ASC
    ) AS posicao,

    jogador1,
    jogador2,
    tempo_segundos,
    resultado,
    data_partida

FROM partidas

WHERE resultado = 'VITORIA'

ORDER BY tempo_segundos ASC;
```

---

## 🚧 Próximas etapas

* [x] Definição da estrutura da tabela
* [x] Definição dos campos
* [x] Definição da regra do ranking
* [x] SQL inicial
* [ ] Conexão com SQLite
* [ ] Inserção automática das partidas
* [ ] API para comunicação com o banco
* [ ] Endpoint para registrar partidas
* [ ] Endpoint para consultar ranking
* [ ] Integração com o jogo Unity
* [ ] Integração com o site
* [ ] Página de ranking online

---

## 🔌 Integração futura

Após a implementação da API, o jogo deverá enviar os dados da partida através de uma requisição HTTP.

Exemplo:

```json
{
    "jogador1": "Victor",
    "jogador2": "João",
    "tempo_segundos": 278.43,
    "resultado": "VITORIA"
}
```

A API ficará responsável por validar os dados e armazená-los no SQLite.

---

## 📝 Observação para a equipe

> **TODO:** Conectar ao SQLite e implementar a inserção automática dos dados das partidas.

Os dados de teste ainda não foram adicionados. A tabela deverá receber informações reais posteriormente através da integração com o jogo/API.

---

## 👥 Projeto

Sistema de ranking desenvolvido como parte do projeto do jogo.

### Tecnologias

* 🎮 Unity
* 🗄️ SQLite
* 🐍 Python / API
* 🌐 Front-end Web
* 🔗 REST API

---

## 📄 Status

**Em desenvolvimento 🚧**

A estrutura inicial do banco já foi definida. As próximas etapas envolvem a implementação da persistência dos resultados e integração com a API e o site.

```
```
