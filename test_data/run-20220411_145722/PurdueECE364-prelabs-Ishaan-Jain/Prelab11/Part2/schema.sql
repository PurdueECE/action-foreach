CREATE TABLE users(
    first_name TEXT,
    id INTEGER PRIMARY KEY);


CREATE TABLE posts(content TEXT,id INTEGER PRIMARY KEY);

INSERT INTO users VALUES( "ishaan",1);
INSERT INTO users VALUES( "jain", 2);
INSERT INTO users VALUES( "ben", 3);
INSERT INTO users VALUES( "allison", 4);
INSERT INTO users VALUES( "bailey", 5);

INSERT INTO posts VALUES("heyyy", 1);
INSERT INTO posts VALUES("I am", 2);
INSERT INTO posts VALUES("amazing", 3);
INSERT INTO posts VALUES("you", 4);
INSERT INTO posts VALUES("are too", 5);


--DELETE from users WHERE first_name LIKE "ishaan";

CREATE TRIGGER aft_del AFTER DELETE ON users
BEGIN
    DELETE from posts WHERE id = OLD.id;
END;