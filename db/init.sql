-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS locadora;
USE locadora;

-- Tabela de Categorias (categories)
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Tabela de Filmes (Movies)
CREATE TABLE movies (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    release_year INT,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE
);

-- Tabela de Popularidade (Popularity)
CREATE TABLE popularity (
    popularity_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    views INT DEFAULT 0,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id) ON DELETE CASCADE
);

-- Inserções na Tabela Categories
INSERT INTO categories (name) VALUES 
('Ação'), 
('Romance'), 
('Comédia'),
('Drama'),
('Terror'),
('Animação');

-- Inserções na Tabela Movies, incluindo todas as categorias
INSERT INTO movies (title, release_year, category_id) VALUES
('Filme Ação 1', 2022, 1),  -- 'Ação' tem ID 1
('Filme Romance 1', 2021, 2),  -- 'Romance' tem ID 2
('Filme Comédia 1', 2020, 3),  -- 'Comédia' tem ID 3
('Filme Drama 1', 2023, 4),  -- 'Drama' tem ID 4
('Filme Terror 1', 2021, 5),  -- 'Terror' tem ID 5
('Filme Animação 1', 2022, 6),  -- 'Animação' tem ID 6
('Filme Ação 2', 2022, 1),  -- 'Ação' tem ID 1
('Filme Romance 2', 2023, 2),  -- 'Romance' tem ID 2
('Filme Comédia 2', 2021, 3);  -- 'Comédia' tem ID 3

-- Inserções na Tabela Popularidade, adicionando os novos filmes
INSERT INTO popularity (movie_id, views) VALUES
(1, 150),  -- Filme Ação 1
(2, 75),   -- Filme Romance 1
(3, 120),  -- Filme Comédia 1
(4, 90),   -- Filme Drama 1
(5, 60),   -- Filme Terror 1
(6, 130),  -- Filme Animação 1
(7, 200),  -- Filme Ação 2
(8, 50),   -- Filme Romance 2
(9, 180);  -- Filme Comédia 2
