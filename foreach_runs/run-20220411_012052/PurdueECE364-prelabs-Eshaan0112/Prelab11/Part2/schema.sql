CREATE TABLE users(
    userID int primary key,
    firstName text,
    lastName text,
    house_no int, 
    area int
); 

CREATE TABLE posts (
    userID int,
    postID int primary key,
    number_of_members int,
    bike_racks_install int,
    satisfaction int,
    CONSTRAINT user_constraint
    FOREIGN KEY (userID)
    REFERENCES users(userID)
);

CREATE TRIGGER del AFTER DELETE ON users
BEGIN 
    DELETE FROM posts WHERE userID=OLD.userID;
END;
