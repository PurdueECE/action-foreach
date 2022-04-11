-- Use part2.db as database
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    username text NOT NULL
);

CREATE TABLE IF NOT EXISTS posts(
    postid INTEGER PRIMARY KEY,
    userid INTEGER NOT NULL,
    title text,
    content text
);

INSERT INTO users VALUES(15, "Jack23");
INSERT INTO users VALUES(16, "SmileyFace");
INSERT INTO users VALUES(17, "Ha&Ha");
INSERT INTO users VALUES(18, "I am Tommy");
INSERT INTO users VALUES(19, "Stanpy");
INSERT INTO users VALUES(20, "Christine");

INSERT INTO posts VALUES(3200, 15, "Hello", "I'm new.");
INSERT INTO posts VALUES(3201, 15, "Hello2", NULL);
INSERT INTO posts VALUES(3202, 17, "Hello3", "I'm new three.");
INSERT INTO posts VALUES(3203, 17, NULL, "I'm new for.");
INSERT INTO posts VALUES(3204, 17, NULL, NULL);
INSERT INTO posts VALUES(3205, 20, "Hello6", "I'm new six.");

CREATE TRIGGER delete_posts AFTER DELETE on users
FOR EACH ROW
BEGIN
    DELETE FROM posts WHERE posts.userid = old.id;
END;
