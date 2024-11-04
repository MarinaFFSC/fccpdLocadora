-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS locadora;
USE locadora;

-- Tabela de Categorias (Categories)
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Tabela de Filmes (Movies)
CREATE TABLE Movies (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    release_year INT,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

-- Tabela de Popularidade (Popularity)
CREATE TABLE Popularity (
    popularity_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    views INT DEFAULT 0,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
);

-- Inserções na Tabela Categories
INSERT INTO Categories (name) VALUES ('Ação'), ('Romance'), ('Comédia');

-- Inserções na Tabela Movies
INSERT INTO Movies (title, release_year, category_id) VALUES
('Filme Ação 1', 2022, 1),
('Filme Romance 1', 2021, 2),
('Filme Comédia 1', 2020, 3),
('Filme Ação 2', 2022, 1),
('Filme Romance 2', 2023, 2),
('Filme Comédia 2', 2021, 3);

-- Inserções na Tabela Popularidade
INSERT INTO Popularity (movie_id, views) VALUES
(1, 150),  -- Filme Ação 1
(2, 75),   -- Filme Romance 1
(3, 120),  -- Filme Comédia 1
(4, 200),  -- Filme Ação 2
(5, 50),   -- Filme Romance 2
(6, 180);  -- Filme Comédia 2
