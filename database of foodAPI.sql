CREATE DATABASE food_db;
USE food_db;
CREATE TABLE foods (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    protein FLOAT NOT NULL,
    fat FLOAT NOT NULL,
    carbs FLOAT NOT NULL
);
INSERT INTO foods (name, protein, fat, carbs) 
VALUES ('Egg', 13, 10, 1);
INSERT INTO foods (name, protein, fat, carbs)
VALUES ('Rice', 4.2, 0.3, 28.7);

SELECT * FROM foods;
