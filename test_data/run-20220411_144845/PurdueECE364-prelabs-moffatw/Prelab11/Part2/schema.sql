CREATE TABLE users (
    id int NOT NULL primary key,
    user_name text NOT NULL
);

CREATE TABLE posts (
    id int NOT NULL primary key,
    user_name text NOT NULL,
    post_name text NOT NULL,
    post_content text NOT NULL
);

INSERT INTO users (id, user_name) VALUES 
    (1, "Will 1"),
    (2, "Will 2"),
    (3, "Will 3"),
    (4, "Will 4"),
    (5, "Will 5");

INSERT INTO posts (id, user_name, post_name, post_content) VALUES 
    (1, "Will 1", "Post 1", "My first post"),
    (2, "Will 2", "Post 2", "My second post"),
    (3, "Will 3", "Post 3", "My third post"),
    (4, "Will 4", "Post 4", "My fourth post"),
    (5, "Will 5", "Post 5", "My fifth post");

CREATE TRIGGER aft_del AFTER DELETE ON users
BEGIN
    DELETE FROM posts WHERE user_name IN(SELECT deleted.user_name FROM deleted);
END;