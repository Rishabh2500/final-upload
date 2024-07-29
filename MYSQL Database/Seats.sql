-- db creation:-
CREATE DATABASE book ;
CREATE TABLE IF NOT EXISTS book.users(
    id INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    number INT(200) NOT NULL,
    name VARCHAR(200)
);
-- insertion:-
INSERT INTO book.users(number,name)
VALUES
(101,'keshav'),
(101,'prasad');

SELECT * FROM `book`.`users` LIMIT 1000;
-- updation:-
UPDATE users   
SET name="Nitish Vashisth"
WHERE id=2;

SELECT * FROM `book`.`users` LIMIT 1000;

INSERT INTO book.users(number,name)
VALUES
(103,'PriyaRaj'),
(104,'David');