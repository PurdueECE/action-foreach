CREATE TABLE users(
    id int primary key NOT NULL,
    login text NOT NULL,
    password text NOT NULL
);

CREATE TABLE posts(
    postid int NOT NULL,
    title text NOT NULL
);

INSERT INTO users (id, login, password) VALUES
    (1, 'login1','pass1'), 
    (2, 'login2','pass2'), 
    (3, 'login3','pass3'), 
    (4, 'login4','pass4'), 
    (5, 'login5','pass5');

 INSERT INTO posts (postid, title) VALUES
    (1, 'title1'), 
    (1, 'title2'), 
    (3, 'title3'), 
    (4, 'title4'), 
    (5, 'title5');

CREATE TRIGGER delete_posts AFTER DELETE ON users
BEGIN
    DELETE FROM posts where postid = OLD.id;
END;