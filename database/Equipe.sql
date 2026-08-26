  CREATE TABLE IF NOT EXISTS equipe (
    id_dev INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    turma VARCHAR(100) NOT NULL,
    funcao VARCHAR(100) NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO equipe (nome, turma, funcao) VALUES
    ("nome": "Amanda Hiromi Nakayoshi", "turma": "Desenvolvimento de Jogos", "funcao": "Game Designer"),
    ("nome": "Ariany de Sousa dos Santos", "turma": "Desenvolvimento de Jogos", "funcao": "Game Designer");
    

SELECT * FROM equipe WHERE id_dev = 1;

UPDATE equipe SET funcao = "Sound Designer" WHERE id_dev = 1;

DELETE FROM equipe WHERE id_dev = 1;

SELECT COUNT(*) AS total FROM equipe;

SELECT * FROM equipe ORDER BY criado_em DESC LIMIT 5;



json
[
  {
    "id_dev": 1,
    "nome": "Amanda Hiromi Nakayoshi",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Sound Designer"
  },
  {
    "id_dev": 2,
    "nome": "Ariany de Sousa dos Santos",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Designer"
  },
  {
    "id_dev": 3,
    "nome": "Beatriz Paes Leme Rego",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Designer"
  },
  {
    "id_dev": 4,
    "nome": "Ben Allan Xavier de Menezes e Silva",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Sound Designer"
  },
  {
    "id_dev": 5,
    "nome": "Caio César Lopes Lima",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Developer"
  },
  {
    "id_dev": 6,
    "nome": "Daniel de Freitas Alves",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Artist"
  },
  {
    "id_dev": 7,
    "nome": "Guilherme Gomes dos Santos",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Artist"
  },
  {
    "id_dev": 8,
    "nome": "Gustavo Henrique Pereira de Brito",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Designer"
  },
  {
    "id_dev": 9,
    "nome": "Heitor André Monteiro Teles de Souza",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Designer"
  },
  {
    "id_dev": 10,
    "nome": "Heloisa Stefany Silva Farias",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Sound Designer"
  },
  {
    "id_dev": 11,
    "nome": "Hugo Costa Barbosa",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Developer"
  },
  {
    "id_dev": 12,
    "nome": "Isadora dos Santos Corrêa",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Artist"
  },
  {
    "id_dev": 13,
    "nome": "João Guilherme Santos Saraiva",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Designer"
  },
  {
    "id_dev": 14,
    "nome": "João Hélio Aragão Borges Sampaio",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Sound Designer"
  },
  {
    "id_dev": 15,
    "nome": "João Victor de Oliveira Souza",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Sound Designer"
  },
  {
    "id_dev": 16,
    "nome": "João Víctor Almeida Costa",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Designer"
  },
  {
    "id_dev": 17,
    "nome": "Julia Eduarda Lago Silva",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Artist"
  },
  {
    "id_dev": 18,
    "nome": "Luiz Filipe Sobral da Cruz",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Sound Designer"
  },
  {
    "id_dev": 19,
    "nome": "Luiz Guilherme Araujo Ferreira",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Developer"
  },
  {
    "id_dev": 20,
    "nome": "Maria Eduarda Santos Barreto",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Artist"
  },
  {
    "id_dev": 21,
    "nome": "Maria Heloísa Pereira de Souza",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Artist"
  },
  {
    "id_dev": 22,
    "nome": "Matheus Farias Feitoza",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Developer"
  },
  {
    "id_dev": 23,
    "nome": "Miguel Antonio de Souza Oliveira",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Artist"
  },
  {
    "id_dev": 24,
    "nome": "Nathan de Souza Dias Cardoso",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Artist"
  },
  {
    "id_dev": 25,
    "nome": "Pedro Henrique Guimaraes Pires",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Sound Designer"
  },
  {
    "id_dev": 26,
    "nome": "Reuel Gomes de Magalhães",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Developer"
  },
  {
    "id_dev": 27,
    "nome": "Vitoria Lorrane Dias da Silva",
    "turma": "Desenvolvimento de Jogos",
    "funcao": "Game Artist"
  },
  {
    "id_dev": 28,
    "nome": "Andre Gualberto Lacerda Veiga",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Game Artist"
  },
  {
    "id_dev": 29,
    "nome": "Arthur Martins Santana",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Back-End Programmer"
  },
  {
    "id_dev": 30,
    "nome": "Arthur Radel Alves",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Back-End Programmer"
  },
  {
    "id_dev": 31,
    "nome": "Bento Matheus Oliveira Nobre",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Front-End Programmer"
  },
  {
    "id_dev": 32,
    "nome": "Caio Leonardo de Paula Leite",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Front-End Programmer"
  },
  {
    "id_dev": 33,
    "nome": "Dâmila Kaliane Cardozo Catão Borges",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Database Engineer"
  },
  {
    "id_dev": 34,
    "nome": "Daniel Tavares Ferreira da Silva",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Database Engineer"
  },
  {
    "id_dev": 35,
    "nome": "Davi Lucas Silva Rodrigues",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Back-End Programmer"
  },
  {
    "id_dev": 36,
    "nome": "Erick Luiz Follmann Vieira",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Game Artist"
  },
  {
    "id_dev": 37,
    "nome": "Esther Vitorya Alvarenga Seabra",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Database Engineer"
  },
  {
    "id_dev": 38,
    "nome": "Heloisa Flor Silva de Araújo",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Database Engineer"
  },
  {
    "id_dev": 39,
    "nome": "Henrique Mendes Martins",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Back-End Programmer"
  },
  {
    "id_dev": 40,
    "nome": "Ian Carneiro da Silva Fernandes",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Database Engineer"
  },
  {
    "id_dev": 41,
    "nome": "Joao Duarte Mendes Siqueira",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "System Analyst"
  },
  {
    "id_dev": 42,
    "nome": "João Freitas Hosken Cunha",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Front-End Programmer"
  },
  {
    "id_dev": 43,
    "nome": "Joao Guilherme Nunes de Lima",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Front-End Programmer"
  },
  {
    "id_dev": 44,
    "nome": "Juan Pablo dos Santos Passos",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Front-End Programmer"
  },
  {
    "id_dev": 45,
    "nome": "Leonardo Mafra Silva Junior",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Database Engineer"
  },
  {
    "id_dev": 46,
    "nome": "Marcos Paulo Alves Borges",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Back-End Programmer"
  },
  {
    "id_dev": 47,
    "nome": "Marcos Vinícius Rodrigues Soares",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Back-End Programmer"
  },
  {
    "id_dev": 48,
    "nome": "Maria Júlia Martins Soares Araújo",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Front-End Programmer"
  },
  {
    "id_dev": 49,
    "nome": "Pedro Branco Paiva",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Front-End Programmer"
  },
  {
    "id_dev": 50,
    "nome": "Pedro Daniel Claudino Martins",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Game Artist"
  },
  {
    "id_dev": 51,
    "nome": "Pedro Henrique Varela Gomes",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Front-End Programmer"
  },
  {
    "id_dev": 52,
    "nome": "Rafael da Silva Bandeira",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Front-End Programmer"
  },
  {
    "id_dev": 53,
    "nome": "Raquelly Luiza Soares Bileu",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Back-End Programmer"
  },
  {
    "id_dev": 54,
    "nome": "Ryan Silva Gomes Pinto",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Database Engineer"
  },
  {
    "id_dev": 55,
    "nome": "Sara Borges Aguiar",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Front-End Programmer"
  },
  {
    "id_dev": 56,
    "nome": "Sarah Layane dos Santos Leitao",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Front-End Programmer"
  },
  {
    "id_dev": 57,
    "nome": "Victor Daniel Spíndola de Oliveira Santos",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Front-End Programmer"
  },
  {
    "id_dev": 58,
    "nome": "Victor de Oliveira Merencio",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Database Engineer"
  },
  {
    "id_dev": 59,
    "nome": "Vitória Alves de Oliveira",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Back-End Programmer"
  },
  {
    "id_dev": 60,
    "nome": "Vitória dos Santos Gonçalves",
    "turma": "Desenvolvimento de Sistemas",
    "funcao": "Back-End Programmer"
  }
]