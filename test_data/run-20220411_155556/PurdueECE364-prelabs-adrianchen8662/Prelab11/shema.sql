CREATE TABLE IF NOT EXISTS users (firstname varchar(255), lastname varchar(255), id INTEGER PRIMARY KEY, email varchar(255));
CREATE TABLE IF NOT EXISTS posts (post_id INTEGER, time varchar(255), content varchar(255), upvotes INTEGER, downvotes INTEGER);


CREATE TRIGGER aft_ins AFTER DELETE ON users
FOR EACH ROW
BEGIN
    DELETE * FROM posts WHERE (SELECT id FROM users) NOT IN post_id
END;
