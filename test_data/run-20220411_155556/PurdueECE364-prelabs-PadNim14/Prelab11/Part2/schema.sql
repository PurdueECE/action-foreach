CREATE TABLE users(
    id int primary key,
    username text,
    password text
);

CREATE TABLE posts (
    id int primary key,
    title text ,
    username text,
    likes int
);

INSERT INTO users VALUES(1, "npadmana", "123");
INSERT INTO users VALUES(2, "josho", "huen1r");
INSERT INTO users VALUES(3, "kuru", "1ase");
INSERT INTO users VALUES(4, "spidey123", "senses");
INSERT INTO users VALUES(5, "bacot", "5inal4");

INSERT INTO posts VALUES(2,"intro", "josho", 100);
INSERT INTO posts VALUES(1,"first", "npadmana", 200);
INSERT INTO posts VALUES(3,"second", "kuru", 300);
INSERT INTO posts VALUES(4,"third", "spidey123", 40);
INSERT INTO posts VALUES(5,"fourth", "bacot", 100000);
-- DELETE from users WHERE username LIKE "npadmana";
-- Ran this command in the sqlite3 terminal version and removed it fine

CREATE TRIGGER aft_del AFTER DELETE ON users
BEGIN
    DELETE from posts WHERE id = OLD.id;
END;



