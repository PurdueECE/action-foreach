CREATE TABLE users(username TEXT,id INTEGER PRIMARY KEY);

CREATE TABLE posts(content TEXT, postid INTEGER PRIMARY KEY, userid INTEGER);

INSERT INTO users VALUES( "siddM",10);
INSERT INTO users VALUES( "suhuM", 13);
INSERT INTO users VALUES( "anuM", 15);
INSERT INTO users VALUES( "amitM", 19);
INSERT INTO users VALUES( "sophC", 1);

INSERT INTO posts VALUES("hello world2", 1, 10);
INSERT INTO posts VALUES("I am Sidd", 2, 10);
INSERT INTO posts VALUES("how are you2", 3, 10);
INSERT INTO posts VALUES("wyd2", 4, 10);
INSERT INTO posts VALUES("#bored2", 5, 10);

CREATE TRIGGER aft_del AFTER DELETE ON users
BEGIN
    DELETE from posts WHERE userid = OLD.id;
END;