CREATE TABLE users (
    id int primary key NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    email text NOT NULL
);

CREATE TABLE posts (
    author_id int NOT NULL,
    post text NOT NULL
);

INSERT INTO users (id, first_name, last_name, email) VALUES 
    (1, 'William', 'Jorge', 'jorge.william@university.com'),
    (2, 'Will', 'Smith', 'smith.will@university.com'),
    (3, 'Chris', 'Rock', 'rock.chris@university.com'),
    (4, 'Jada', 'Pinkett', 'pinkett.jada@university.com'),
    (5, 'Willow', 'Smit', 'smith.willow@university.com');

INSERT INTO posts (author_id, post) VALUES 
    (2, 'I dont regret it'),
    (3, 'How could he do that'),
    (4, 'Just nod and smile...'),
    (5, 'Caught a vibe, baby are you coming for the ride'),
    (1, 'So hungry right now'),
    (2, 'And I would do it again');

CREATE TRIGGER aft_del AFTER DELETE ON users
BEGIN
    DELETE FROM posts WHERE author_id=OLD.id;
END;