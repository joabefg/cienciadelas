  CREATE TABLE IF NOT EXISTS FAQ (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    perguntas VARCHAR(100) NOT NULL,
    respostas VARCHAR(500) NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO FAQ (perguntas, respostas) VALUES
    ("O que é o Ciência Delas?", "Ciência Delas é um jogo de cartas cooperativo em que dois jogadores trabalham juntos para enfrentar uma ameaça global. Inspirado na importância das mulheres na ciência, o jogo combina estratégia, gerenciamento de recursos e tomada de decisões."),
    ("Quem são as personagens jogáveis?", "Você poderá jogar com duas cientistas inspiradas em mulheres que marcaram a história da ciência:\n- Marie Curie\n- Jaqueline Goes de Jesus\nCada uma possui habilidades e cartas exclusivas."),
    ("Como funciona a cooperação?", "Os jogadores compartilham recursos como Saúde, Infraestrutura e Pesquisa, precisando planejar suas ações em conjunto para superar os desafios da ameaça."),
    ("Por que o jogo se chama Ciência Delas?", "Porque busca destacar o protagonismo feminino na ciência por meio de uma experiência educativa e estratégica baseada em cientistas que marcaram a história e a ciência contemporânea.");

--Consulta dos dados

SELECT * FROM FAQ WHERE id = 1;

UPDATE FAQ SET perguntas = "Quem são as personagens jogáveis??" WHERE id = 1;

DELETE FROM FAQ WHERE id = 1;

SELECT COUNT(*) AS total FROM FAQ;

SELECT * FROM FAQ ORDER BY criado_em DESC LIMIT 5;


json
    [
  {
    "id": 0,
    "pergunta": "O que é o Ciência Delas?",
    "resposta": "Ciência Delas é um jogo de cartas cooperativo em que dois jogadores trabalham juntos para enfrentar uma ameaça global. Inspirado na importância das mulheres na ciência, o jogo combina estratégia, gerenciamento de recursos e tomada de decisões."
  },
  {
    "id": 1,
    "pergunta": "Quem são as personagens jogáveis?",
    "resposta": "Você poderá jogar com duas cientistas inspiradas em mulheres que marcaram a história da ciência:\n- Marie Curie\n- Jaqueline Goes de Jesus\nCada uma possui habilidades e cartas exclusivas."
  },
  {
    "id": 2,
    "pergunta": "Como funciona a cooperação?",
    "resposta": "Os jogadores compartilham recursos como Saúde, Infraestrutura e Pesquisa, precisando planejar suas ações em conjunto para superar os desafios da ameaça."
  },
  {
    "id": 3,
    "pergunta": "Por que o jogo se chama Ciência Delas?",
    "resposta": "Porque busca destacar o protagonismo feminino na ciência por meio de uma experiência educativa e estratégica baseada em cientistas que marcaram a história e a ciência contemporânea."
  }
]