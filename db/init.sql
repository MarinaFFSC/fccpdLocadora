-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS locadora;
USE locadora;

CREATE TABLE IF NOT EXISTS Categorias(
	categoria_id INT AUTO_INCREMENT PRIMARY KEY,
	categoria_nome VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Filmes(
	filme_id VARCHAR(30) PRIMARY KEY,
	filme_nome VARCHAR(50) NOT NULL,
	filme_ano INT,
	filme_descricao VARCHAR(500) NOT NULL,
	filme_estoque INT,
	filme_alugados INT DEFAULT 0,
	filme_categoria_id INT NOT NULL,
	FOREIGN KEY (filme_categoria_id) REFERENCES Categorias(categoria_id)
);

CREATE TABLE IF NOT EXISTS Aluguel(
	aluguel_id INT AUTO_INCREMENT PRIMARY KEY,
	aluguel_filme_id VARCHAR(30) NOT NULL,
	aluguel_cliente_nome VARCHAR(100) NOT NULL,
	FOREIGN KEY (aluguel_filme_id) REFERENCES Filmes(filme_id)
);

CREATE TABLE IF NOT EXISTS Clientes(
	cliente_nome VARCHAR(100) NOT NULL PRIMARY KEY,
	cliente_login VARCHAR(50) NOT NULL,
	cliente_senha VARCHAR(50) NOT NULL,
	cliente_alugado_id INT,
	FOREIGN KEY (cliente_alugado_id) REFERENCES Aluguel(aluguel_id)
);



SHOW TABLES;


-- ADICIONANDO EM CLIENTE O ADMINISTRADOR
SELECT * FROM Clientes;
INSERT INTO Clientes VALUES('Admin', 'admin', 'admin', DEFAULT);
INSERT INTO Clientes VALUES('Roberto', 'robb', 'robb', DEFAULT);
	

-- ADICIONANDO AS CATEGORIAS
SELECT * FROM Categorias;
INSERT INTO Categorias (categoria_nome) VALUES ('ACAO'), ('ROMANCE'), ('TERROR'), ('COMEDIA'), ('FICCAO'), ('DRAMA'), ('ANIMACAO');


-- ADICIONANDO AOS FILMES
SELECT * FROM Filmes;
INSERT INTO Filmes VALUES('134711', 'Vingadores', 2012, 'Brincando de Heroi', 7, DEFAULT, 1);
INSERT INTO Filmes VALUES('082211', 'A Culpa e das Estrelas', 2014, 'Triste.', 3, DEFAULT, 2);
INSERT INTO Filmes VALUES('172611', 'O Chamado', 2002, 'Aquela menina da TV', 9, DEFAULT, 3);
INSERT INTO Filmes VALUES('065911', 'O Diabo Veste Prada', 2006, 'Ela so queria um emprego...', 1, DEFAULT, 4);
INSERT INTO Filmes VALUES('213711', 'Star Wars IV', 1997, 'Anakin, nao faca isso', 16, DEFAULT, 5);
INSERT INTO Filmes VALUES('000011', 'Taxi Driver', 1976, 'Motorista Maluco', 11, DEFAULT, 6);
INSERT INTO Filmes VALUES('180411', 'Frozen', 2014, 'Entorpecentes', 9, DEFAULT, 7);
INSERT INTO Filmes VALUES('135811', 'IT', 2017, 'Nunca confie em palhaços', 0, DEFAULT, 3);

