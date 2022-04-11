CREATE TABLE users (
    username STRING PRIMARY KEY,
    password STRING
    );

CREATE TABLE posts (
    pid STRING PRIMARY KEY,
    user STRING,
    content TEXT
    );




INSERT INTO users (username, password) VALUES("user0", "pass0");
INSERT INTO users (username, password) VALUES("user1", "pass1");
INSERT INTO users (username, password) VALUES("user2", "pass2");
INSERT INTO users (username, password) VALUES("user3", "pass3");
INSERT INTO users (username, password) VALUES("user4", "pass4");

INSERT INTO posts (pid, user, content) VALUES("0", "user0","TESTING 0");
INSERT INTO posts (pid, user, content) VALUES("1", "user1","TESTING 1");
INSERT INTO posts (pid, user, content) VALUES("2", "user2","TESTING 2");
INSERT INTO posts (pid, user, content) VALUES("3", "user3","TESTING 3");
INSERT INTO posts (pid, user, content) VALUES("4", "user4","TESTING 4");

CREATE TRIGGER aft_del AFTER DELETE ON 
users   
BEGIN
    DELETE FROM posts WHERE user = OLD.username
END;